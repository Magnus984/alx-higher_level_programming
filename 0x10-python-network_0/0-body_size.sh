#!/usr/bin/bash
# Takes URL, sends request to URl and displays the size of the body response.
echo $(echo "$(curl -s -I "$1")" | grep -i 'Content-Length' | awk '{print $2}')
