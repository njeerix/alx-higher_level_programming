#!/usr/bin/node

const request = require('request');

// Retrieve the API URL from the command line argument
const apiUrl = process.argv[2];

// Check if API URL argument is provided
if (!apiUrl) {
	console.error('Usage: ./6-completed_tasks.js <api-url>');
	process.exit(1);
}

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

	// Parse the JSON response body into an array of task objects
	const tasks = JSON.parse(body);

	// Initialize an object to store the count of completed tasks per user
	const completedTasksByUser = {};

	// Iterate through the tasks to count completed tasks per user ID
	tasks.forEach(task => {
		// Check if the task is completed (completed === true)
		if (task.completed) {
			// Increment the completed tasks count for the user ID
			if (completedTasksByUser[task.userId]) {
				completedTasksByUser[task.userId]++;
			} else {
				completedTasksByUser[task.userId] = 1;
			}
		}
	});

	console.log(completedTasksByUser);
});
