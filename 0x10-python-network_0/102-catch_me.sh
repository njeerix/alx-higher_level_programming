#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that causes the server
curl -s -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me
