import re
import sys
import pathlib

import asyncio
from bs4 import BeautifulSoup

from async_utils import run_requests
import async_linker
from constants import RANK
from taxonomic_trees import Tree
from async_calls import Mem, load_set, divide_chunks, make_requests, dump_set, grab_href


def grab_href(tag):
    try:
        href = tag["href"]

        # don't clean links twice
        if href in mem.cleaned_links:
            return
        mem.cleaned_links.add(href)

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
    here = pathlib.Path(__file__).parent

    TAXA = "Mammalia"
    PATTERN = re.compile(r"(/wiki/\w+:)")
    RANK_SET = set(RANK)

    mem = Mem()

    mem.root = "https://en.wikipedia.org/wiki/"

    mem.all_links = load_set("dump_all.txt") | {TAXA}
    mem.seen_links = load_set("dump_seen.txt")
    mem.biota_links = load_set("dump_biota.txt")
    mem.cleaned_links = set()

    while any(mem.all_links - mem.seen_links):
        urls = list(mem.all_links - mem.seen_links)

        print("To check:", len(urls))
        for subset in divide_chunks(urls, 100):
            mem.seen_links |= set(subset)
            subset = list(mem.root + x for x in subset)

            first = True
            for url, status, html in run_requests(subset):
                if TAXA not in html or ".biota" not in html:
                    print(".", end="")
                    continue

                soup = BeautifulSoup(html, "lxml")
                box = soup.select_one(".biota")

                if box is None or TAXA not in str(box):
                    print(".", end="")
                    continue

                url = url[len(mem.root):]

                if not first:
                    print()
                else:
                    first = False
                print(url, end="")

                mem.updated = True
                body = soup.select_one("#content")
                mem.biota_links.add(url)

                mem.all_links |= set(filter(bool, map(grab_href, box.select("a") + body.select("a"))))

            print(
                "Dumping links:",
                ", ".join(map(str, (
                    len(mem.all_links),
                    len(mem.seen_links),
                    len(mem.biota_links)
                )))
            )
            dump_set("dump_all.txt", mem.all_links)
            if len(mem.seen_links) > 1:
                dump_set("dump_seen.txt", mem.seen_links)
            if mem.biota_links:
                dump_set("dump_biota.txt", mem.biota_links)

    print("Total checked:", len(mem.seen_links))

    # filename = f"{TAXA}_{dt.strftime(dt.now(), '%Y%m%dT%H%M%S')}.txt"
    filename = TAXA + ".txt"

    with open(filename, "w") as f:
        f.write("\n".join(sorted(mem.biota_links)))

    # run the linking portion
    async_linker.main(TAXA)

    cladogram = Tree.from_csv("Mammalia.csv")

    # print(cladogram.pretty_str())
    # cladogram.prune(rank="Family", includes=re.compile(r"\bCanidae\b", re.I))
    # print(cladogram.from_pov("Canis"))
    # cladogram.view()
    # cladogram.search(r"\bbat\b", case_insensitive=True)
    # cladogram.to_csv("output.csv")

    # with open("output.txt", "w") as f:
    #     f.write(cladogram.pretty_str(with_color=False))
