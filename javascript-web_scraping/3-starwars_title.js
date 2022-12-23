#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;
request.get({ url: url, json: true }, function (error, response, body) {
  if (process.argv[2] && !error && response.statusCode === 200) console.log(body.title);
});
