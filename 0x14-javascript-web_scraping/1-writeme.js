#!/usr/bin/node

const fs = require('fs');

// Retrieve the file path and string to write from command line arguments
const file = process.argv[2];
const string = process.argv[3];

// Write the content to the specified file in utf-8 encoding
fs.writeFile(file, string, 'utf-8', function (err) {
  if (err) console.log(err);
});
