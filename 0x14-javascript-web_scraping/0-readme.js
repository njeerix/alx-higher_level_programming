#!/usr/bin/node

const fs = require('fs');

// Retrieve the file path fom the first command line argument
const filePath = process.argv[2];

// Check if a file path argument was provided
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    // Print the error object if an error occurred during reading
    console.error(err);
  } else {
    // Print the content of the file if reading was successful
    console.log(data);
  }
});
