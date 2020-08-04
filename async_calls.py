import os
import re
import sys
import lxml
import time
import pathlib
import asyncio
import aiohttp
from datetime import datetime as dt
from asyncio.exceptions import TimeoutError
from aiohttp import ClientSession, ClientConnectorError
from bs4 import BeautifulSoup, Tag


os.system("clear")

TAXA = "Mammalia"
PATTERN = re.compile(r"(/wiki/\w+:)")


class Mem:
    def __init__(self):
        pass


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


async def fetch_html(url, session):
    trials = 0
    while trials < 3:
        try:
            async with session.get(url) as resp:
                return url, await resp.text()
        except Exception as e:
            print(e)
            time.sleep(10)
        trials += 1


async def make_requests(urls):
    async with ClientSession() as session:
        tasks = [fetch_html(url=url, session=session) for url in urls]
        results = await asyncio.gather(*tasks)

    first = True
    for url, html in filter(bool, results):
        if TAXA not in html or "biota" not in html:
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

        mem.all_links |= set(
            filter(bool, map(grab_href, box.select("a") + body.select("a"))))
    print()


def divide_chunks(lst, length):
    for index in range(0, len(lst), length):
        yield lst[index:index + length]


def dump_set(filename, set_):
    with open(filename, "w") as f:
        f.write("\n".join(map(str, set_)))


def load_set(filename):
    with open(filename) as f:
        return set(f.read().split("\n"))


if __name__ == "__main__":
    assert sys.version_info >= (3, 7), "Script requires Python 3.7+"
    here = pathlib.Path(__file__).parent

    mem = Mem()

    mem.root = "https://en.wikipedia.org/wiki/"

    mem.all_links = load_set("dump_all.txt")
    mem.seen_links = load_set("dump_seen.txt")
    mem.biota_links = load_set("dump_biota.txt")
    mem.cleaned_links = set()

    while any(mem.all_links - mem.seen_links):

        urls = list(mem.all_links - mem.seen_links)
        print("To check:", len(urls))
        for subset in divide_chunks(urls, 100):
            mem.seen_links |= set(subset)
            subset = (mem.root + x for x in subset)
            asyncio.run(make_requests(urls=subset))

            print(
                "Dumping links:",
                ", ".join(map(str, (
                    len(mem.all_links),
                    len(mem.seen_links),
                    len(mem.biota_links)
                )))
            )
            dump_set("dump_all.txt", mem.all_links)
            dump_set("dump_seen.txt", mem.seen_links)
            dump_set("dump_biota.txt", mem.biota_links)

    print("Total checked:", len(mem.seen_links))

    # filename = f"{TAXA}_{dt.strftime(dt.now(), '%Y%m%dT%H%M%S')}.txt"
    filename = TAXA + ".txt"

    with open(filename, "w") as f:
        f.write("\n".join(sorted(mem.biota_links)))
