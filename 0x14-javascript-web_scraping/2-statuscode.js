#!/usr/bin/node

const request = require('request');

// Retrieve the URL from the command line argument
const url = process.argv[2];

// Check if URL argument is provided
if (!url) {
  console.error('Usage: ./2-statuscode.js <URL>');
  process.exit(1);
}

// Perform a GET request to the specified URL
request.get(url, (error, response) => {
  if (error) {
    // Print the error if request encounters an error
    console.error(error);
  } else {
    // Print the status code from the response
    console.log(`code: ${response.statusCode}`);
  }
});
