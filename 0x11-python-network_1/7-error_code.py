#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and
displays the body of the response
"""

import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    reque = requests.get(url)

    if reque.status_code >= 400:
        print(f"Error code: {}".format(reque.status_code))
    else:
        print(reque.text)
