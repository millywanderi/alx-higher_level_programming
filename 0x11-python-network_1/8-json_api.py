#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests

if __name__ == '__main__':
    lett = "" if len(sys.argv) == 1 else sys.argv[1]
    pload = {"q": lett}

    resp = requests.post("http://0.0.0.0:5000/search_user", data=pload)
    try:
        resp_json = resp.json()
        if resp_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(resp_json.get("id"), resp_json.get("name")))
    except ValueError:
        print("Not a valid JSON")
