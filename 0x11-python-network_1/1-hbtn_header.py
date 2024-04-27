#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and dispays the value of the
X-request-Id variable found in the header of the response.
"""
import sys
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        header_value = response.getheader("X-Request-Id")
        print(header_value)
