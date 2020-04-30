"""
Threading is creating multiple threads under single process and play around. They share memory, and resources.
Its optimised to not to create more than 10 threads, and to make it thread-safe, write code cautious, & use Queue.

https://realpython.com/python-concurrency/
..date..    Apr 11 2020
"""


# Synchronous Version
import requests
import time
#
#
# def download_site(url, session):
#     with session.get(url) as response:
#         print(f"Read {len(response.content)} from {url}")
#
#
# def download_all_sites(sites):
#     with requests.Session() as session:
#         for url in sites:
#             download_site(url, session)
#
#
# if __name__ == "__main__":
#     sites = [
#         "https://www.jython.org",
#         "http://olympus.realpython.org/dice",
#     ] * 80
#     start_time = time.time()
#     download_all_sites(sites)
#     duration = time.time() - start_time
#     print(f"Downloaded {len(sites)} in {duration} seconds")


# Asynchronous Version

import concurrent.futures
import threading

#
#
# thread_local = threading.local()
#
#
# def get_session():
#     if not hasattr(thread_local, "session"):
#         thread_local.session = requests.Session()
#     return thread_local.session
#
#
# def download_site(url):
#     session = get_session()
#     with session.get(url) as response:
#         print(f"Read {len(response.content)} from {url}")
#
#
# def download_all_sites(sites):
#     with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
#         executor.map(download_site, sites)
#
#
# if __name__ == "__main__":
#     sites = [
#         "https://www.jython.org",
#         "http://olympus.realpython.org/dice",
#     ] * 80
#     start_time = time.time()
#     download_all_sites(sites)
#     duration = time.time() - start_time
#     print(f"Downloaded {len(sites)} in {duration} seconds")


fake = [x for x in range(400)]
a = list()


def write_to_list(data):
    a.append(data)


def do_something(data):
    time.sleep(random.randrange(2, 6))
    write_to_list(data)


start_time = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as execuor:
    execuor.map(do_something, fake)

duration = time.time() - start_time
print(f"Appended {len(a)} in {duration} seconds")
