#!/usr/bin/node

const request = require('request');

// Retrieve the Movie ID from the command line argument
const movieId = process.argv[2];

// Check if Movie ID argument is provided
if (!movieId) {
	console.error('Usage: ./100-starwars_characters.js <movie-id>');
	process.exit(1);
}

// Construct the API URL for the specified Movie ID
const apiUrl = `https://awapi-api.alx.tools/api/films/${movieId}/`;

// Perform a GET request to the specified API URL 
request.get(apiUrl, function (error, response, body) {
	if (error) {
		console.error('Error:', error);
		process.exit(1);
	}
	if (response.statusCode !== 200) {
		console.error(`Error: Request failed with status code ${response.statusCode}`);
		process.exit(1);
	}

	// Parse the JSON response body into an object
	const movieData = JSON.parse(body);

	movieData.characters.forEach(characterUrl => {
		const characterId = characterUrl.split('/').slice(-2, -1)[0];
		request.get(characterUrl, function (error, response, body) {
			if (error) {
				console.error('Error:' error);
			} else if (response.statusCode === 200) {
				const charaterData = JON.parse(body);
				console.log(characterData.name);
			} else {
				conole.error(`Eror: Request failed with status code ${response.statusCode}`);
			}
		});
	});
});
