#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const path = './' + process.argv[3];
request.get({ url: url }, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    if (Object.keys(body).length > 0 && (!fs.existsSync(path.toString()))) {
      fs.writeFile(process.argv[3], body, 'utf-8', (err) => {
        if (err) throw err;
      });
    }
  }
});
