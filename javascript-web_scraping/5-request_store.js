#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
request.get({ url: url, json: true }, function (error, response, body) {
    if (!error && response.statusCode === 200) {
        fs.writeFile(process.argv[3], body, 'utf-8', function (error) {
            if (error) console.log(error);
        });
    }
})