#!/usr/bin/node

// Get the size of the square from the first arguments and convert it to an integer
const size = parseInt(process.argv[2]);

// Check if the argument can be converted to an integer and if it's not print "Missing size"
if (isNaN(size)) {
  console.log('Missing size');
} else {
  // loop through rows to print the square
  for (let i = 0; i < size; i++) {
    // Create a string representing a row of the square filled with 'X'
    const row = 'X'.repeat(size);
    // Print the row
    console.log(row);
  }
}
