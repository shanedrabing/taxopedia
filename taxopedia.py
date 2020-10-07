import re
import sys
import pickle
from pprint import pprint
from bs4 import BeautifulSoup

from async_utils import run_requests, divide_chunks


# CONSTANTS


PATTERN = re.compile(r"(/wiki/\w+:)")


# FUNCTIONS


def load_set(filename):
    try:
        with open(filename) as f:
            return set(f.read().split("\n"))
    except FileNotFoundError:
        return set()


def dump_set(filename, set_):
    with open(filename, "w") as f:
        f.write("\n".join(map(str, set_)))


def load_dict(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {
            "root": "https://en.wikipedia.org/wiki/",
            "all": load_set("dump_all.txt"),
            "seen": load_set("dump_seen.txt"),
            "biota": load_set("dump_biota.txt"),
            "cleaned": set()
        }


def dump_dict(filename, dict_):
    with open(filename, "wb") as f:
        pickle.dump(dict_, f)


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


if __name__ == "__main__":
    assert sys.version_info >= (3, 7), "Script requires Python 3.7+"

    # use-defined parameters
    TAXA = "Canidae"
    COMPREHENSIVE = False

    # keep a dictionary of links
    links_dict = load_dict(TAXA)

    # if nothing loaded, make sure to start with search term
    links_dict["all"].add(TAXA)

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

            first = True
            for url, status, html in run_requests(subset):
                # filter out pages:
                # without a biota box
                if "biota" not in html:
                    print(".", end="")
                    continue

                # parse the page
                soup = BeautifulSoup(html, "lxml")

                # find the biota box
                box = soup.select_one(".biota")

                # filter out boxes:
                # without mention of search term
                if box is None or TAXA not in str(box):
                    print(".", end="")
                    continue

                # remove root from extension
                url = url[len(links_dict["root"]):]

                if not first:
                    print()
                else:
                    first = False
                print(url, end="")

                body = soup.select_one("#content")
                links_dict["biota"].add(url)

                to_check = box.select("a")
                if COMPREHENSIVE:
                    to_check += body.select("a")

                new_links = set()
                for link in to_check:
                    href = grab_href(link, links_dict)
                    if href:
                        new_links.add(href)
                links_dict["all"] |= new_links
            print()

            # save the dictionary
            dump_dict(TAXA, links_dict)

        # update remaining links
        links_dict["remaining"] = links_dict["all"] - links_dict["seen"]

    # how many links did we check?
    print("Total checked:", len(links_dict["seen"]))

    pprint(links_dict)

    # filename = f"{TAXA}_{dt.strftime(dt.now(), '%Y%m%dT%H%M%S')}.txt"
    # filename = TAXA + ".txt"

    # with open(filename, "w") as f:
    #     f.write("\n".join(sorted(links_dict["biota"])))
