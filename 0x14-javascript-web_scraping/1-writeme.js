#!/usr/bin/node

const fs = require('fs');

// Retrieve the file path and string to write from command line arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Check if both file path and content arguments are provided
if (!filePath || !content) {
  console.error('Usage: ./1-writeme.js <file-path> "<string-to-write>"');
  process.exit(1);
}

// Write the content to the specified file in utf-8 encoding
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    // Print the error object if an error occurred during writing
    console.error(err);
  } else {
    // Output a success message if writing was successful
    console.log(`Content was written to ${filePath}`);
  }
});
