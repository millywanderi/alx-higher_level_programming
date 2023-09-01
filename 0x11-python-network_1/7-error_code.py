#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and
displays the body of the response
"""

import requests
import sys


__name__ == '__main__':
    url = sys.argv[1]
    reque = requests.get(url)

    if reque.statusCode >= 400:
        print(f"Error code: {reque.statusCode}")
    else:
        print(reque.text)
