#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    payload = {}
    if len(sys.argv) <= 1:
        payload['q'] = ""
    else:
        payload['q'] = sys.argv[1]
    req = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
