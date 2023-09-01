#!/usr/bin/python3
"""script that takes 2 arguments in order to solve this challenge."""
from sys import argv
import requests

if __name__ == '__main__':
    repo = argv[1]
    owner = argv[2]

    url = 'https://api.github.com/repos/{}/{}/\
            commits?per_page=10'.format(owner, repo)
    r = requests.get(url)
    r = r.json()

    for commit in r:
        print('{}: {}'.format(commit.get('sha'),
                              commit.get('commit').get('author').get('name')))
