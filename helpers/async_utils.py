import asyncio
import selectors
from aiohttp import ClientSession, ClientConnectorError


async def fetch_html(url, session):
    try:
        async with session.get(url) as resp:
            return url, resp.status, await resp.text()
    except ClientConnectorError:
        pass


async def make_requests(urls):
    async with ClientSession() as session:
        tasks = (fetch_html(url, session) for url in urls)
        return await asyncio.gather(*tasks)


def run_requests(urls):
    """ url, status, html """
    selector = selectors.SelectSelector()
    loop = asyncio.SelectorEventLoop(selector)
    result = loop.run_until_complete(make_requests(urls))
    loop.close()    
    return result


def divide_chunks(lst, length):
    for index in range(0, len(lst), length):
        yield lst[index:index + length]


if __name__ == "__main__":
    x = run_requests(["https://en.wikipedia.org/wiki/Main_Page"])
    print(x)
