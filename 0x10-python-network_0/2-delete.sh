#!/bin/bash
# Sends a DELETE request to URL and displayes body of response.
echo $(curl -s -X DELETE $1)
