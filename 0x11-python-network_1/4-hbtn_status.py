#!/usr/bin/python3
"""Script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    req = requests.get('https://alx-intranet.hbtn.io/status')
    body = req.text
    print("Body responses:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
