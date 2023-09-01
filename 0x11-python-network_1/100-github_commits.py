#!/usr/bin/python3
"""script that takes 2 arguments in order to solve this challenge."""
from sys import argv
import requests

if __name__ == '__main__':

    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        argv[2], argv[1])
    try:
        respo = requests.get(url)
        resDict = respo.json()
        for i in range(0, 10):
            print("{}: {}".format(resDict[i].get('sha'), resDict[i].get(
                'commit').get('author').get('name')))
    except Exception:
        pass
