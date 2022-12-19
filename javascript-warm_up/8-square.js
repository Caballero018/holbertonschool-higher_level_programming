#!/usr/bin/node
const args = process.argv;
let i = 0;
let j = 0;
let message;
const len = Object.keys(args).length;

if (isNaN(parseInt(args[2])) || len === 2) {
  message = 'Missing size';
  console.log(message);
} else {
  for (i = 0; i <= parseInt(args[2]) - 1; i++) {
    message = '';
    for (j = 0; j <= parseInt(args[2]) - 1; j++) {
      message += 'X';
    }
    console.log(message);
  }
}
