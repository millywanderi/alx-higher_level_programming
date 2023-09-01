#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""
import urllib.request
import sys

if __name__ == "__main__":
    reque = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(reque) as response:
        html = response.info()
        print(html.get("X-Request-Id"))
