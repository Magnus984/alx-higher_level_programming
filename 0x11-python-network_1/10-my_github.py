#!/usr/bin/python3
"""
takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import sys
import requests


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]
    auth = (username, password)
    req = requests.get(url, auth=auth)
    response = req.json()
    print(response.get("id"))
