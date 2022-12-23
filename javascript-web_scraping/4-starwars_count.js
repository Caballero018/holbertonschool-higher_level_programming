#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count = 0;
let i = 0;
request.get({ url: url, json: true }, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    // eslint-disable-next-line no-unused-vars
    for (const dls of body.results) {
      for (const l of body.results[i].characters) {
        if (l.includes(18)) count++;
      }
      i++;
    }
    console.log(count);
  }
});
