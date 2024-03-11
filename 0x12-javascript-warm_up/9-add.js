#!/usr/bin/node

// Define a function namedad that takes two arguments a and b
function add (a, b) {
  // Return the sum of the two integers
  return a + b;
}

// Get the first and second integers from the command line arguments
const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

// Check if both arguments are valid integers
if (isNaN(num1) || isNaN(num2)) {
  // if any arguments is not a valid integer, print NaN
  console.log('NaN');
} else {
  // if both arguments are valid integers, call the add function and print the result
  console.log(add(num1, num2));
}
