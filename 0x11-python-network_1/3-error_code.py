#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
