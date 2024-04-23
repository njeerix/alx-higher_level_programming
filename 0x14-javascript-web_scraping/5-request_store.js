#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Perform a Get request to the specified URL
request(process.argv[2], function (error, response, body) {
	if (error == null) {
		fs.writeFileSync(process.argv[3], body);
	}
});
