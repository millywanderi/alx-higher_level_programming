#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as parameter, and displays the body of the response
"""
import urllib.request
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    emailData = {"email": argv[2]}
    data = urllib.parse.urlencode(emailData).encode("ascii")

    reque = urllib.request.Request(url, data)
    with urllib.request.urlopen(reque) as response:
        print(response.read().decode("utf-8"))
