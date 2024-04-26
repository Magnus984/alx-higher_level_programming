#!/bin/bash
# Takes URL, sends a GET request to the URL and displays the body of the response
echo $(curl -s -L "$1")
