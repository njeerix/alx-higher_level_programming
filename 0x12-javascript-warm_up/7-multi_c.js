#!/usr/bin/node

// Get the first argument of the script and convert into an integer
const x = parseInt(process.argv[2]);

// Check if the argument can be converted to an integer
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  // loop x times and print "Cis fun" each time
  for (let i = 0; i < x; i++) { console.log('C is fun'); }
}
