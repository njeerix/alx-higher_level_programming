#!/usr/bin/node

const request = require('request');

// Retrieve the movie ID from the command line argument
const movieId = process.argv[2];

// Check if movie ID argument is provided and is a valid integer
if (!movieId || isNaN(parseInt(movieId))) {
  console.error('Usage: ./3-starwars_title.js <movie-id>');
  process.exit(1);
}

// Construct the URL with the specified movie ID 
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Perform a Get request to the Star Wars API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    // Print the error if request encounters an error
    console.error(error);
  } else {
    // parse the JSON response body into an object
    const filmData = JSON.parse(body);

    // Check if the movie data was retrieved successfully
    if (response.statusCode === 200) {
      // Print the title of the movie
      console.log(filmData.title);
    } else {
      // Print an error message if the movie ID is invalid or not found
      console.error(`Error: Movie with ID ${movieId} not found`);
    }
  }
});
