#!/usr/bin/node
const args = process.argv;
let i = 0;
let message;
const len = Object.keys(args).length;

if (isNaN(parseInt(args[2])) || len === 2) {
  message = 'Missing number of occurrences';
  console.log(message);
} else {
  message = 'C is fun';
  while (i <= parseInt(args[2]) - 1) {
    console.log(message);
    i++;
  }
}
