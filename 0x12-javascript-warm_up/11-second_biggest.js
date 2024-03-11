#!/usr/bin/node

// Get the arguments passed to the script and convert them to integrs
const args = process.argv.slice(2).map(Number);

// Sort the array of integers in descending order
args.sort((a, b) => b - a);

// If no arguments passed or only one arguments, print 0
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  // Print the second element in the sorted array, which is the second biggest integer
  console.log(args[1]);
}
