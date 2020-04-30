"""
Using Aysnc and await.
it has something called event_loop, which is the task manager, its aware of tasks' states'.
Maintains two lists' - Waiting, Ready.

This is thread-safe as the task will be solely responsible for releasing the resource for use to others, unlike
 threading.

One important point to be taken -- Async doesnt work well with many libraries, need to ensure if that particular lib
 supports asyncio.

..date..    Apr 15 2020
"""

import asyncio
import aiohttp
import time


async def download_site(session, url):
    async with session.get(url) as response:
        print("Read {0} from {1}".format(response.content_length, url))


async def downloadable_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = list()
        for _ in sites:
            task = asyncio.ensure_future(download_site(session, _))
            tasks.append(task)
    await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    start = time.time()
    sites = [
                "https://www.jython.org",
                "http://olympus.realpython.org/dice",
            ] * 80
    asyncio.get_event_loop().run_until_complete(downloadable_sites(sites))
    print(f"total time taken = {time.time()- start}")

