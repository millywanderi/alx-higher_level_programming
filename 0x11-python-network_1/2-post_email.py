#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as parameter, and displays the body of the response
"""
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = {'email': sys.argv[2]}

    email = urllib.parse.urlencode(email)
    reque = urllib.request.Request(url, email)
    with urllib.request.urlopen(reque) as response:
        response = response.read()
        response = response.decode('utf-8')
        print(response)
