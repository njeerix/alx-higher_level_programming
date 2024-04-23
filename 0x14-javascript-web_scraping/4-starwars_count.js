#!/usr/bin/node

const request = require('request');

// Retrieve the API URL from the command line argument
const apiUrl = process.argv[2];

// Check if API URL argument is provided
if (!apiUrl) {
	console.error('Usage: ./4-starwars_count.js <api-url>');
	process.exit(1);
}

// Perform a GET request tothe specified API URL
request(apiUrl, function (error, response, body) {
	if (error) {
		console.error('Errorr:', error);
		return;
	}

	if (response.statusCode !== 200) {
		console.error('Error: API request failed with status code', response.statusCode);
		return;
	}

	// Parse the JSON response body into an object
	const filmsData = JSON.parse(body);

	// Check if 'results' array exists in the response data
	if (!filmsData.results || !Array.isArray(filmsData.results)) {
		console.error('Error: unexpected API response format');
		return;
	}

	// Initialize a counter for movies wuth Wedge Antilles
	let count = 0;
	
	// Iterate through each film object in the 'results' array
	filmsData.results.forEach(film => {
		// Check if 'characters' array exists in the film data
		if (film.characters && Array.isArray(film.characters)) {
			// Check if Wedge Antillies (character ID 18)
			if (film.characters.some(charUrl => charUrl.includes('/18/'))) {
				count++;
			}
		}
	});

	console.log(count);
});
