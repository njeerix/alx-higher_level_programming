#!/usr/bin/node

// Get the first argument passed to the script
const firstArg = process.argv[2];

// Convert the first argument to an integer using parseInt() function
// If the conversion is successful, print "My number: <integer>"
// If the conversion fails (e.g, the argument is not a valid number), print "Not a number"
const parsedInt = parseInt(firstArg);
if (!isNaN(parsedInt)) {
  console.log('My number:', parsedInt);
} else {
  console.log('Not a number');
}
