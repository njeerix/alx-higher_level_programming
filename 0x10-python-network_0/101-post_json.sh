#!/bin/bash
# Sends a JSON POST request to a given URL with a given JSON file.
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <URL> <JSON_file>"
    exit 1
fi

if [ ! -f "$2" ]; then
    echo "File not found: $2"
    exit 1
fi

if ! jq '.' "$2" >/dev/null 2>&1; then
    echo "Not a valid JSON: $2"
    exit 1
fi

curl -s -H "Content-Type: application/json" -d "@$2" "$1"
