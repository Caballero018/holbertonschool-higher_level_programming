#!/usr/bin/node
const request = require('request');
const url = 'https://jsonplaceholder.typicode.com/todos';
request.get({ url: url, json: true }, function (error, response, body) {
  if (!error) {
    const obj = {};
    let count = 1;
    // eslint-disable-next-line no-unused-vars
    for (let i = 1; i <= Object.keys(body).length; i++) {
      for (const dic of body) {
        if (i === dic.userId) {
          if (dic.completed === true) obj[i.toString()] = count++;
        }
      }
      count = 1;
    }
    console.log(obj);
  }
});
