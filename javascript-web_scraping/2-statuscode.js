#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (error, response) {
  if (response.statusCode === 200 && !error) console.log(`code: ${response.statusCode}`);
});
