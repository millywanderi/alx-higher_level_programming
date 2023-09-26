#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, (error, response, body) => {
  if (error) { console.log(error); }
  const jsonBody = JSON.parse(body);
  for (const charURL of jsonBody.characters) {
    request(charURL, (err, m, body) => {
      if (err) { console.log(err); }
      const jsonBody = JSON.parse(body);
      console.log(jsonBody.name);
    });
  }
});
