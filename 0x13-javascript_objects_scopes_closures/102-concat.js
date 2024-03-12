#!/usr/bin/node

const fs = require('fs');

const [, , fileA, fileB, fileC] = process.argv;

fs.readFile(fileA, 'utf8', (err, dataA) => {
	if (err) {
		console.error(err);
		return;
	}

	fs.readFile(fileB, 'utf8', (err, dataB) => {
		if (err) {
			console.error(err);
			return;
		}

		const concatenatedContent = `$[dataA.trim()}\n$}dataB.trim()}\n`;

		fs.writeFile(fileC, concatenatedContent, err => {
			if (err) {
				console.error(err);
				return;
			}
			console.log(`Concatenated content has been written to ${fileC}`);
		});
	});
});
