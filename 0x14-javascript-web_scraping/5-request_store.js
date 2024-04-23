#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Retrieve the URL and file path from command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Check if URL and file path arguments are provided
if (!url || !filePath) {
	console.error('Usage: ./5-request_store.js <url> <file-path>');
	process.exit(1);
}

// Perform a Get request to the specified URL
request.get(url, function (error, response, body) {
	if (error) {
		console.error('Error:', error);
		process.exit(1);
	}

	// Write the response body to the specified file path (UTF-8 encoded)
	fs.writeFile(filePath, body, 'utf-8', function (err) {
		if (err) {
			console.error('Error writing to file:', err);
			process.exit(1);
		}
		console.log(`Web content successfully saved to '${filePath}'`);
	});
});
