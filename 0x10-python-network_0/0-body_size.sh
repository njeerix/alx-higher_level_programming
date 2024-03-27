#!/bin/bash
# This script takes a URL as input, sends a request to that URL using curl
curl -s "$1" | wc -c
