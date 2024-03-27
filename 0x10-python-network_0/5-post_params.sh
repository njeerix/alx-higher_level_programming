#!/bin/bash
# Takes in a URL, sends a POST request to the URL with specified parameter
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
