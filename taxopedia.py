import asyncio
import csv
import functools
import json
import re
import selectors
import urllib
from types import FunctionType
from typing import Dict, Iterable, List, Tuple

import aiohttp
import bs4

# CONSTANTS


class Symbols:
    CROSS = " × "
    DAGGER = "†"
    FLAT = "─"
    VERT = "│"
    RTEE = "├"
    TURN = "└"
    EYE = "👁"


WIKI_EN = "https://en.wikipedia.org/wiki/"
WIKI_IMG = "https://upload.wikimedia.org/"
WIKI_PATTERN = re.compile(r"^(/wiki/[A-z#]+)$")
WIKI_IMG_PATTERN = re.compile(r"/thumb|(/\d+px.*?)$")
SPECIAL = (Symbols.DAGGER, Symbols.CROSS)


RANK = [
    "Domain", "Subdomain", "Realm", "Subrealm", "Hyperkingdom",
    "Superkingdom", "Kingdom", "Subkingdom", "Infrakingdom", "Parvkingdom",
    "Superphylum", "Phylum", "Subphylum", "Infraphylum", "Microphylum",
    "Superclass", "Class", "Subclass", "Infraclass", "Parvclass",
    "Superdivision", "Division", "Subdivision", "Infradivision",
    "Superlegion", "Legion", "Sublegion", "Infralegion", "Supercohort",
    "Cohort", "Subcohort", "Infracohort", "Gigaorder", "Magnorder",
    "Grandorder", "Mirorder", "Superorder", "Series", "Order", "Parvorder",
    "Nanorder", "Hypoorder", "Minorder", "Suborder", "Infraorder",
    "Parvorder", "Section", "Subsection", "Gigafamily", "Megafamily",
    "Grandfamily", "Hyperfamily", "Superfamily", "Epifamily", "Series",
    "Group", "Family", "Subfamily", "Infrafamily", "Supertribe", "Tribe",
    "Subtribe", "Infratribe", "Genus", "Subgenus", "Section", "Subsection",
    "Series", "Subseries", "Superspecies", "Species", "Subspecies", "Hybrid",
    "Variety", "Subvariety", "Form", "Subform"
]


# CLASSES


class WikiTree:
    def __init__(self, key, data=None, children=set()):
        self.key = key
        self.data = data
        self.children = set(children)

        self.parent = None
        self.is_cached = False

    def __str__(self):
        dct = self.data
        if "Common Name" in dct:
            return f"{dct['Header']}: {dct['Label']} ({dct['Common Name']})"
        return f"{dct['Header']}: {dct['Label']}"

    __repr__ = __str__

    def __lt__(self, other):
        return (
            (-self.get_num_children(), self.data["RankN"], str(self)) <
            (-other.get_num_children(), other.data["RankN"], str(other))
        )

    def __iter__(self):
        yield self.parent_data()
        for x in self.sorted_children():
            yield from x

    # travel up the root
    def root(self):
        if self.parent:
            return self.parent.root()
        return self

    def parent_data(self):
        if self.parent:
            return self.parent.parent_data() + (self.data,)
        return (self.data,)

    # return the number of children
    def get_num_children(self):
        return (
            len(self.children) +
            sum(map(WikiTree.get_num_children, self.children))
        )

    def sorted_children(self):
        if not self.is_cached:
            self._sorted_children = sorted(self.children)
            self.is_cached = True
        return self._sorted_children

    # add a child
    def add_child(self, child):
        self.children.add(child)
        self.is_cached = False

    # remove a child
    def remove_child(self, child):
        self.children.remove(child)
        self.is_cached = False

    # POV
    def from_pov(self, key_origin):
        root, *path = self.path_to_root(key_origin)
        prev = root

        for node in path:
            prev.children |= {node}
            prev = node

        return root

    # POV
    def path_to(self, key_origin, key_dest):
        path = self.from_pov(key_dest).path_to_root(key_origin)
        return (x.key for x in path)

    # POV
    def path_to_root(self, key_origin):
        path = self.recursive_rooter(key_origin)
        if not path:
            raise ValueError(f"Node {key_origin} not found")
        return path

    # POV
    def recursive_rooter(self, key_origin):
        if self.key == key_origin:
            self.is_cached = False
            return (self,)
        for child in self.children:
            response = child.recursive_rooter(key_origin)
            if response:
                newkids = {x for x in self.children if x.key != child.key}
                return response + (WikiTree(self.key, self.data, newkids),)

    # pretty print
    def pretty(self, key=None, first="", second="", length=2):
        string = f"{first}{self if key is None else key(self)}\n"
        ordinal = self.sorted_children()

        # everything prior to the last
        for x in ordinal[:-1]:
            string += x.pretty(
                key,
                second + f"{Symbols.RTEE}{Symbols.FLAT * length} ",
                second + f"{Symbols.VERT}{' ' * length} ",
                length
            )

        # the last (or only) child
        if ordinal:
            string += ordinal[-1].pretty(
                key,
                second + f"{Symbols.TURN}{Symbols.FLAT * length} ",
                second + f" {' ' * length} ",
                length
            )

        return string

    def to_txt(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.pretty())

    def to_html(self, filename):
        def key(tree):
            dct = tree.data
            string = f"{dct['Header']}: "
            if "IMAGE" in dct:
                string += (
                    f"<a href='{dct['IMAGE']}'>" +
                    f"<img src='{dct['THUMB']}'></a> "
                )
            if "URL" in dct:
                string += f"<a href='{dct['URL']}'>"
            string += dct["Label"]
            if "Common Name" in dct:
                string += f" ({dct['Common Name']})"
            if "URL" in dct:
                string += "</a>"
            return string

        with open(filename, "w", encoding="utf-8") as f:
            lst = self.pretty(key).split("\n")
            body = "\n".join(map(lambda x: f"<pre>{x}</pre>", lst))
            f.write(f"<html><body>\n{body}\n</html></body>\n")

    def to_csv(self, filename):
        data = list()
        keys = {
            "Rank": -3,
            "Label": -2,
            "Common Name": -1,
            "URL": len(RANK) + 0,
            "IMAGE": len(RANK) + 1,
            "THUMB": len(RANK) + 2
        }

        # iterate through parent data
        for lst in self:
            row = dict()

            # standard data
            for x in lst:
                keys[x["Header"]] = x["RankN"]
                row[x["Header"]] = x["Label"]
                row["Rank"] = x["Header"]
                row["Label"] = x["Label"]

            # extra data
            for k, v in lst[-1].items():
                if k not in ("Rank", "RankN", "Header", "Label"):
                    row[k] = v

            data.append(row)

        # ordered columns
        ordinal = sorted(keys.items(), key=lambda x: x[::-1])
        fields = [k for (k, v) in ordinal]

        # write to file
        with open(filename, "w", newline='') as f:
            writer = csv.DictWriter(f, fields)
            writer.writeheader()
            for row in data:
                writer.writerow(row)


# FUNCTIONS (ASYNC)


async def fetch_html(url: str, session: aiohttp.ClientSession) -> Tuple[str, int, str]:
    """Given a URL and a aiohttp.ClientSession, grab the final URL, status
    code, and HTML

    :param url: A single web-link
    :param session: Usually comes from make_requests function
    :returns: (URL, status code, HTML)
    """
    try:
        async with session.get(url) as resp:
            return (str(resp.url), resp.status, await resp.text())
    except aiohttp.ClientConnectorError:
        pass


async def make_requests(urls: Iterable):
    """Given a list of URLs, fetch many HTMLs

    :param urls: A list of URLS
    :returns: Awaited asyncio.gather object
    """
    async with aiohttp.ClientSession() as session:
        tasks = (fetch_html(url, session) for url in urls)
        return await asyncio.gather(*tasks)


def run_requests(urls: Iterable) -> List[Tuple[str, int, str]]:
    """Wrapper for make_requests, try this for ease of use

    :param urls: A list of URLS
    :returns: A list of tuples (URL, status code, HTML)
    """
    selector = selectors.SelectSelector()
    loop = asyncio.SelectorEventLoop(selector)
    result = loop.run_until_complete(make_requests(urls))
    loop.close()
    return result


# FUNCTIONS (HELPERS)


def get_rank(unit: str) -> int:
    """Return the index position of unit in RANK

    :param unit: The taxonomic unit to be found 
    :returns: The index position of unit in RANK, otherwise None
    """
    if unit in RANK:
        return RANK.index(unit)


def replace_all(string: str, old: str, new: str) -> str:
    """Iteratively replace all instances of old with new

    :param old: String to be acted upon
    :param old: Substring to be replaced
    :param new: String replacement
    :returns: A copy of string with new replacing old
    """
    if old in string:
        string = string.replace(old, new)
    return string


def get_href(link: bs4.element.Tag) -> str:
    """If a link has an href attribute, return it

    :param link: The link to be checked
    :returns: An href
    """
    if (link.has_attr("href")):
        return (link["href"])


def is_wiki_url(url: str) -> bool:
    """If a link is a Wiki page, return True

    :param url: The link to be checked
    :returns: True or false: is the URL a Wiki page?
    """
    return (isinstance(url, str) and WIKI_PATTERN.search(url))


def make_wiki_url(taxon: str) -> str:
    """Ensures generation of a proper Wikipedia URL from taxon

    :param taxon: Either a taxon's common name or scientific name (e.g. "Bear"
        or "Ursidae"). A full or partial Wikipedia link will also be returned.
    :returns: A URL prefixed with "https://en.wikipedia.org/wiki/"
    """
    pre = (taxon if taxon.startswith("http") else "//" + taxon)
    parsing = urllib.parse.urlparse(pre)

    if (parsing.netloc in WIKI_EN):
        suffix = urllib.parse.urlunparse(parsing)
    else:
        suffix = taxon

    url = urllib.parse.urljoin(WIKI_EN, suffix)
    return (url.split("#")[0])


def make_img_url(src: str) -> Tuple[str, str]:
    """Given an image source, generate thumbnail and full image URLs

    :param src: Partial URL from <img src="?">
    :returns: Both the thumbnail URL and full image URL
    """
    thumb = urllib.parse.urljoin(WIKI_IMG, src)
    full = WIKI_IMG_PATTERN.sub("", thumb)
    return (thumb, full)


# FUNCTIONS (TAXOPEDIA)


def process_request(request: tuple, check: str, comprehensive: bool) -> Tuple[set, bs4.element.Tag]:
    """Given a single Wikipedia page `request` (url, status, html); find the
    biota box, if applicable, and all links on either the whole page if
    `comprehensive`, or just the biota box. If using the `check` parameter,
    then it must be found in the biota box, otherwise the function with return
    early.

    :param request: URL, status code, and HTML of a single Wikipedia page
    :param check: Taxon checked within the biota box (keeps searches small)
    :param comprehensive: Should the search include all page links?
    :returns: A set of links to check next and the biota box
    """
    # unpack variable
    (url, status, html) = request

    # check status code; for biota box
    if (status != 200 or "biota" not in html):
        return set(), None

    # parse html
    soup = bs4.BeautifulSoup(html, "lxml")
    box = soup.select_one(".biota")

    # must have biota box
    if (not box or (isinstance(check, str) and check not in str(box))):
        return set(), None

    # get links from biota box, and body if comprehensive
    links = box.select("a")
    if (comprehensive):
        body = soup.select_one("#content")
        links += body.select("a")

    # process new links
    hrefs = filter(is_wiki_url, map(get_href, links))
    newurls = set(map(make_wiki_url, hrefs))

    return (newurls, box)


def process_request_closure(check: str, comprehensive: bool) -> FunctionType:
    """For use in functional applications (map, filter, etc.)

    :param check: Taxon checked within the biota box (keeps searches small)
    :param comprehensive: Should the search include all page links?
    :returns: A function (process_request), preloaded with parameters
    """
    def f(request: tuple) -> Tuple[set, bs4.element.Tag]:
        return process_request(request, check, comprehensive)
    return f


def process_biota_box(box: bs4.element.Tag, url: str) -> dict:
    """Scrape naming, taxonomic, and image data from the biota box

    :param box: The bs4 tag to be parsed
    :param url: The associated url of the biota box
    :returns: A dictionary full of parsed data
    """
    # initialize our dictionary
    biota = {
        (-1, "URL"): str(url)
    }

    # find the common name of this taxon
    name = (
        box.select_one("th").get_text("|")
        .split("|")[0].strip()
    )
    biota[(-1, "Common Name")] = name

    # find the image link (if there is one)
    img = box.select_one(".image > img")
    if img and img.has_attr("src"):
        thumb, full = make_img_url(img["src"])
        biota[(-1, "THUMB")] = thumb
        biota[(-1, "IMAGE")] = full

    # make sure we see "Scientific Classification"
    postsci = False

    # find the from the biota box
    for x in box.select("tr"):
        if "get_text" not in dir(x):
            continue

        for junk in x.select("small"):
            junk.extract()

        text = " ".join(x.get_text("|").split())
        header, *lst = (
            replace_all(text, "| |", "|")
            .strip("| ").split("|")
        )

        if header == "Scientific classification":
            postsci = True
        elif postsci and header.endswith(": "):
            header = header.strip(": ")
            rank = get_rank(header)

            if not rank:
                continue

            # remove notes
            lst = [x for x in lst if not x.startswith("[")]
            lststr = " ".join(lst)

            if any(map(lststr.__contains__, SPECIAL)):
                # special cases
                biota[(rank, header)] = replace_all(lststr, "  ", " ")
            else:
                # do not allow unranked classifications
                lst = (tuple(lst) if len(lst) > 1 else lst[0])
                biota[(rank, header)] = lst

    # find the rank of this taxon
    (level, _) = max(biota.items())
    biota[(-1, "Rank")] = level

    return biota


def make_bag(term: str, check: str, comprehensive: bool) -> Tuple[Dict]:
    """Walk out a iterative search through Wikipedia pages for biota boxes that
    contain `check`, starting at the redirected Wiki page from `term`, and
    using all the page links if `comprehensive` is True

    :param term: Starting term, usually suffix of "en.wikipedia.org/wiki/?"
    :param check: Taxon checked within the biota box (keeps searches small)
    :param comprehensive: Should the search include all page links?
    :returns: The parsed results of all the visited pages
    """
    # starting off
    hold = make_wiki_url(term)
    urls = {hold}
    scraper = process_request_closure(check, comprehensive)

    # checked links
    seen = set()

    # loop
    biota_bag = tuple()
    while urls:
        plural = ("s" if len(urls) > 1 else "")
        print("Now checking", len(urls), f"link{plural}...")

        # requesting and parsing
        requests = run_requests(urls)
        url_sets, boxes = zip(*map(scraper, requests))

        # saving the valid boxes
        for request, box in zip(requests, boxes):
            if (box is not None):
                (url, *_) = request
                biota = process_biota_box(box, url)
                biota_bag += (biota,)

                # update restriction
                if (url == hold) and (check is None):
                    check = biota[biota[(-1, "Rank")]]
                    print(
                        f"Now requesting \"{check}\"\n" +
                        "  (otherwise, set `check` parameter manually)"
                    )
                    scraper = process_request_closure(check, comprehensive)

        # only need to check new links
        urls = functools.reduce(set.union, url_sets)
        urls -= seen
        seen |= urls

    print("Done!\n")
    return biota_bag


def dump_bag(filename: str, bag: Tuple[Dict]) -> None:
    """Used for saving a biota bag

    :param filename: A filename for writing
    """
    with open(filename, "w") as f:
        json.dump(tuple(map(lambda x: tuple(x.items()), bag)), f)


def load_bag(filename: str) -> Tuple[Dict]:
    """Used for loading a biota bag

    :param filename: A filename for reading
    :returns: A biota bag
    """
    with open(filename, "r") as f:
        return tuple(
            {
                tuple(k): tuple(v) if isinstance(v, list) else v
                for k, v in biota
            }
            for biota in json.load(f)
        )


def make_tree(biota_bag: Tuple[Dict]) -> WikiTree:
    """From a list of parsed biota boxes (dict), add the data to WikiTree
    nodes, link the nodes together, and return the root of the tree

    :param biota_bag: A list of dictionaries with biota information 
    :returns: A full tree from the collection of biota boxes
    """
    # for finding already created nodes
    nodes = dict()

    # for each organism
    for dct in biota_bag:
        extra = dict()
        parent_key = None

        for (rank, header), label in sorted(dct.items()):
            if (rank == -1):
                # extra data
                extra[header] = label
                continue

            # standard information
            data = {
                "RankN": rank,
                "Header": header,
                "Label": label
            }

            # assign key
            child_key = label
            if child_key not in nodes:
                if (rank == extra["Rank"][0]):
                    # representative (has data)
                    nodes[child_key] = WikiTree(child_key, {**data, **extra})
                else:
                    # strutural (only has label)
                    nodes[child_key] = WikiTree(child_key, data)

            # connect
            if parent_key in nodes:
                child = nodes[child_key]
                parent = nodes[parent_key]

                # add or update parent
                if child.parent is None:
                    child.parent = parent
                    parent.add_child(child)
                elif child.parent is not parent:
                    if parent.data["RankN"] > child.parent.data["RankN"]:
                        child.parent.remove_child(child)
                        child.parent = parent
                        parent.add_child(child)

            # child key is now the parent key
            parent_key = child_key

        # update common names
        temp = nodes[child_key].data
        header = "Common Name"
        common = extra[header]
        if (header in temp and common not in temp[header]):
            common = ", ".join((
                temp[header], common
            ))
        temp[header] = common

    # all done
    root = child.root()
    return root


def arboretum(term: str, check: str = None, comprehensive: bool = False) -> Tuple[WikiTree, Tuple[Dict]]:
    """Starting with a single search `term`, grow a WikiTree through an
    iterative web-crawler; if the search is `comprehensive`, it will include
    all the links on each page; if `check` is set to a specific taxon, it must
    be found in a biota box for that box to be considered valid

    :param term: Starting term, usually suffix of "en.wikipedia.org/wiki/?"
    :param check: Taxon checked within the biota box (keeps searches small)
    :param comprehensive: Should the search include all page links?
    :returns: A WikiTree and the parsed results of all the visited pages
    """
    biota_bag = make_bag(term, check, comprehensive)
    tree = make_tree(biota_bag)
    return (tree, biota_bag)
