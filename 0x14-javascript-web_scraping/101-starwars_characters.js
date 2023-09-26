#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, async (error, response, body) => {
  if (error) { console.log(error); }
  const jsonBody = JSON.parse(body);

  for (const charURL of jsonBody.characters) {
    await new Promise((resolve, reject) => {
      request(charURL, (err, m, body) => {
        if (err) {
          reject(err);
        } else {
          const jsonBody = JSON.parse(body);
          console.log(jsonBody.name);
          resolve();
        }
      });
    });
  }
});
