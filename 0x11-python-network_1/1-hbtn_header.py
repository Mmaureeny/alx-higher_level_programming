#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL and displays the value """
import urllib.request
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        info_page = response.info()
        print(info_page.get('X-Request-Id'))
