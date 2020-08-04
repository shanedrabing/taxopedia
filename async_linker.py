import os
import re
import sys
import random
import pickle
import urllib
import asyncio
import aiohttp
import unicodedata
from aiohttp import ClientSession, ClientConnectorError
from collections import defaultdict

import pandas as pd
from utils import wd_join
from bs4 import BeautifulSoup


TAXA = "Mammalia"

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

RANK_SET = set(RANK)


def my_normalize(word):
    return unicodedata.normalize("NFKC", word)


def dedupe(iterable, *, key=None):
    seen = set()
    for x in iterable:
        if key:
            proxy = key(x)
        else:
            proxy = x
        if proxy not in seen:
            yield x
            seen.add(proxy)


async def fetch_html(url, session):
    try:
        async with session.get(url) as resp:
            return url, await resp.text()
    except ClientConnectorError:
        pass


async def make_requests(urls):
    async with ClientSession() as session:
        tasks = [fetch_html(url=url, session=session) for url in urls]
        results = await asyncio.gather(*tasks)

    for url, html in filter(bool, results):
        filename = url.split("/")[-1] + ".html"
        print("Now parsing:", filename)
        soup = BeautifulSoup(html, "lxml")
        text = soup.select_one(".biota")

        with open(wd_join(TAXA, filename), "w") as f:
            f.write(str(text))


def divide_chunks(lst, length):
    for index in range(0, len(lst), length):
        yield lst[index:index + length]


if not os.path.exists(wd_join(TAXA)):
    os.mkdir(wd_join(TAXA))

to_add = []
with open(wd_join(f"{TAXA}.txt")) as f:
    urls = f.read().split("\n")
    for href in urls:
        filename = href + ".html"
        if not os.path.exists(wd_join(TAXA, filename)):
            to_add.append("https://en.wikipedia.org/wiki/" + href)

for subset in divide_chunks(to_add, 100):
    asyncio.run(make_requests(subset))

files = os.listdir(wd_join(TAXA))

htmls = []
for fname in files:
    with open(wd_join(TAXA, fname)) as f:
        html = f.read()
        if "Ancestral taxa" in html:
            os.remove(wd_join(TAXA, fname))
        else:
            htmls.append(html)

pattern = re.compile(r"(>(.*?)<)")

data = []
for html in htmls:
    soup = BeautifulSoup(html, "lxml")

    traits = []
    for x in soup.find("tbody").children:
        try:
            _, matches = iter(zip(*pattern.findall(" ".join(str(x).split()))))
            matches = map(str.strip, matches)
            traits += iter(map(my_normalize, filter(bool, matches)))
        except AttributeError:
            pass
        except ValueError:
            pass

    try:
        my_index = traits.index("Scientific classification")
    except ValueError:
        my_index = -1

    dictionary = {"Common Name": traits[0]}

    prev = ""
    order = ["Common Name"]

    iterator = iter(traits[1 + my_index:])
    for curr in iterator:
        if prev.istitle() and prev.endswith(":"):
            prev = prev.rstrip(":")
            if prev not in RANK_SET:
                continue

            if curr == "†":
                curr += next(iterator)
            dictionary[prev] = curr
            order.append(prev)
        prev = curr

    dictionary["Rank"] = order[-1]
    if order[-1] == "Species":
        try:
            sp = dictionary["Species"]
            gn = dictionary["Genus"]
            dictionary["Species"] = sp.replace(gn[0] + ".", gn)
        except KeyError:
            pass
    data.append(dictionary)


def key_sort(key):
    try:
        return RANK.index(key)
    except ValueError:
        return float("inf")


def rank_sort(row):
    return RANK.index(row["Rank"])


all_keys = sorted(
    set(key for line in data for key in line.keys()),
    key=key_sort
)

data.sort(key=rank_sort)

df = pd.DataFrame(dedupe(data, key=repr))[all_keys]
df.to_csv(wd_join(f"{TAXA}.csv"), index=False)
