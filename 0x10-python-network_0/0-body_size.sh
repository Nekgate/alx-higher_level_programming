#!/bin/bash
# This takes in a URL, send a request to that URL, and displays the size of the of the response.
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
