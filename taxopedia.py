import re
import sys
import pickle
from pprint import pprint
from bs4 import BeautifulSoup

from async_utils import run_requests, divide_chunks


# CONSTANTS


PATTERN = re.compile(r"(/wiki/\w+:)")

RANK = [
    "Rank", "Common Name", "Domain", "Subdomain", "Realm", "Subrealm",
    "Hyperkingdom", "Superkingdom", "Kingdom", "Subkingdom", "Infrakingdom",
    "Parvkingdom", "Superphylum", "Phylum", "Subphylum", "Infraphylum",
    "Microphylum", "Superclass", "Class", "Subclass", "Infraclass",
    "Parvclass", "Superdivision", "Division", "Subdivision", "Infradivision",
    "Superlegion", "Legion", "Sublegion", "Infralegion", "Supercohort",
    "Cohort", "Subcohort", "Infracohort", "Gigaorder", "Magnorder",
    "Grandorder", "Mirorder", "Superorder", "Series", "Order", "Parvorder",
    "Nanorder", "Hypoorder", "Minorder", "Suborder", "Infraorder",
    "Parvorder", "Section", "Subsection", "Gigafamily", "Megafamily",
    "Grandfamily", "Hyperfamily", "Superfamily", "Epifamily", "Series",
    "Group", "Family", "Subfamily", "Infrafamily", "Supertribe", "Tribe",
    "Subtribe", "Infratribe", "Genus", "Subgenus", "Section", "Subsection",
    "Series", "Subseries", "Superspecies", "Species", "Subspecies",
    "Variety", "Subvariety", "Form", "Subform"
]


# FUNCTIONS


def load_dict(search_term):
    try:
        with open(search_term + ".search", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {
            "root": "https://en.wikipedia.org/wiki/",
            "all": set(),
            "seen": set(),
            "biota": set(),
            "cleaned": set(),
            "search_term": search_term,
        }


def dump_dict(search_term, dict_):
    with open(search_term + ".search", "wb") as f:
        pickle.dump(dict_, f)


def per_result(result, links_dict):
    # expand result
    url, status, html = result

    # filter out pages:
    # without a biota box
    if "biota" not in html:
        return

    # parse the page
    soup = BeautifulSoup(html, "lxml")

    # find the biota box
    box = soup.select_one(".biota")

    # filter out boxes:
    # without mention of search term
    if box is None or links_dict["search_term"] not in str(box):
        return

    # remove root from extension
    url = url[len(links_dict["root"]):]

    body = soup.select_one("#content")
    links_dict["biota"].add(url)

    to_check = box.select("a")
    if links_dict["comprehensive"]:
        to_check += body.select("a")

    new_links = set()
    for link in to_check:
        href = grab_href(link, links_dict)
        if href:
            new_links.add(href)
    links_dict["all"] |= new_links


def grab_href(tag, links_dict):
    try:
        href = tag["href"]

        # don't clean links twice
        if href in links_dict["cleaned"]:
            return
        links_dict["cleaned"].add(href)

        # make sure it's a wiki page
        if not href.startswith("/wiki/"):
            return

        # don't want files, templates, etc.
        if PATTERN.search(href):
            return
        href = href[6:]

        # add wikipedia, remove section
        # href = "https://en.wikipedia.org" + href
        sublink = href.rfind("#")
        if sublink != -1:
            href = href[:sublink]

        return href
    except KeyError:
        return


def search(search_term, comprehensive=False):
    # keep a dictionary of links
    links_dict = load_dict(search_term)
    links_dict["comprehensive"] = comprehensive

    # if nothing loaded, make sure to start with search term
    links_dict["all"].add(search_term)

    # find remaining links
    links_dict["remaining"] = links_dict["all"] - links_dict["seen"]

    # loop as long as links still remain
    while any(links_dict["remaining"]):
        urls = list(links_dict["remaining"])

        # how many links do we have to check?
        print("To check:", len(urls))
        for subset in divide_chunks(urls, 50):
            # have seen these links
            links_dict["seen"] |= set(subset)

            # add root to extension
            subset = (links_dict["root"] + x for x in subset)
            for result in run_requests(subset):
                per_result(result, links_dict)

            # save the dictionary
            dump_dict(search_term, links_dict)

        # update remaining links
        links_dict["remaining"] = links_dict["all"] - links_dict["seen"]

    # how many links did we check?
    print("Total checked:", len(links_dict["seen"]))
    return links_dict


if __name__ == "__main__":
    assert sys.version_info >= (3, 7), "Script requires Python 3.7+"

    # scrape
    links_dict = search("Canidae", False)

    # link

    # explore
