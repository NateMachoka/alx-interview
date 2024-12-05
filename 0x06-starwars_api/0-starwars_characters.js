#!/usr/bin/node

const request = require('request');

// Retrieve the Movie ID from command-line arguments
const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// Construct the API URL
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

// Make a request to the Star Wars API to get the movie details
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;

  // Fetch and print each character's name in the correct order
  fetchCharacters(characters, 0);
});

// Recursive function to handle character requests in sequence
function fetchCharacters(characters, index) {
  if (index >= characters.length) {
    return;
  }

  request(characters[index], (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }

    const character = JSON.parse(body);
    console.log(character.name);

    // Proceed to the next character
    fetchCharacters(characters, index + 1);
  });
}
