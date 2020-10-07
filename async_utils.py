import os
from bs4 import BeautifulSoup

import asyncio
import aiohttp
import aiofiles
from aiohttp import ClientSession, ClientConnectorError


async def fetch_html(url, session):
    try:
        async with session.get(url) as resp:
            return url, resp.status, await resp.text()
    except ClientConnectorError:
        pass


async def fetch_file(url, filepath, session):
    try:
        print(url, filepath)
        if not os.path.exists(filepath):
            async with session.get(url) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(filepath, mode='wb')
                    await f.write(await resp.read())
                    await f.close()
    except aiohttp.ClientConnectorError:
        pass


async def make_requests(urls):
    async with ClientSession() as session:
        tasks = (fetch_html(url, session) for url in urls)
        return await asyncio.gather(*tasks)


async def make_downloads(urls, filepaths):
    async with ClientSession() as session:
        tasks = (
            fetch_file(url, fname, session)
            for url, fname in zip(urls, filepaths)
        )
        await asyncio.gather(*tasks)


def run_requests(urls):
    """ url, status, html """
    return asyncio.run(make_requests(urls))


def divide_chunks(lst, length):
    for index in range(0, len(lst), length):
        yield lst[index:index + length]
