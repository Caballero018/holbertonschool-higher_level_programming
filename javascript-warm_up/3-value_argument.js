#!/usr/bin/node
const args = process.argv;
let message;
let len = 0;

// eslint-disable-next-line no-unused-vars
for (const arg in args) {
  len += 1;
}

if (len > 2) {
  console.log(args[2]);
} else {
  message = 'No argument';
  console.log(message);
}
