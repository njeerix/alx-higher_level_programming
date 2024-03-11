#!/usr/bin/node

// Define a function named factorial that takes an integer n as arguments
function factorial (n) {
  // Base case: if n is NaN or less than or equal to 1, return 1
  if (isNaN(n) || n <= 1) {
    return 1;
  } else {
    // Recursive case: return n times the factorial of (n - 1)
    return n * factorial(n - 1);
  }
}

// Get the integer from the command line arguments
const num = parseInt(process.argv[2]);

// Compute the factorial using the factorial function and print the result
console.log(factorial(num));
