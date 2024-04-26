#!/bin/bash
# Takes in a URL and displays all the HTTP requests the server will accept.
echo $(echo "$(curl -s -I "$1")" | grep -i 'allow' | awk '{$1=""; print $0}')
