#!/usr/bin/node
const args = process.argv;
let message;
const len = Object.keys(args).length;
let int;

if (len === 3) {
  int = parseInt(args[2]);
  if (isNaN(int)) {
    message = 'Not a number';
  } else {
    message = `My number: ${int}`;
  }
  console.log(message);
} else {
  message = 'Not a number';
  console.log(message);
}
