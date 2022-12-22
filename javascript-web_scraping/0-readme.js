#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', function (error, data) {
    if (data) {
        console.log(data);
    } else {
        throw error;
    }
});
