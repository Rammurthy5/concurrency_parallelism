"""
Multiprocessing helps creates separate process and do the needful. it is thread-safe as it doesnt share resources.
This helps if we have CPU-bound tasks in the program.

..date..    Apr 15 2020
"""

import multiprocessing
import requests
import time

# This is an example for using multiprocessing for a I/O bound tasks. Shows ineffective.
# session = None
#
#
# def get_session():
#     global session
#     if not session:
#         session = requests.Session()
#
#
# def download_site(site):
#     with session.get(site) as response:
#         name = multiprocessing.current_process().name
#         print(f"{name}:Read {len(response.content)} from {site}")
#
#
# def downloadable_sites(sites):
#     with multiprocessing.Pool(initializer=get_session) as pool:
#         pool.map(download_site, sites)
#
#
# if __name__ == "__main__":
#     start = time.time()
#     sites = [
#                 "https://www.jython.org",
#                 "http://olympus.realpython.org/dice",
#             ] * 80
#     downloadable_sites(sites)
#     print(f"total time taken = {time.time()- start}")
#

# Here's an instance of using synchronous CPU bound program
#
#
# def get_total(number):
#     return sum([x for x in range(number)])
#
#
# def find_sums():
#     for _ in range(29392, 78929):
#         get_total(_)
#
#
# if __name__ == "__main__":
#     start = time.time()
#     find_sums()
#     print(f"total time taken = {time.time()- start}")     # 208 secs


# Here is an instance to run the same code above with MP

def get_total(number):
    return sum([x for x in range(number)])


def find_sums():
    with multiprocessing.Pool() as pool:
        pool.map(get_total, range(29392, 78929))


if __name__ == "__main__":
    start = time.time()
    find_sums()
    print(f"total time taken = {time.time()- start}")       # 91 secs
