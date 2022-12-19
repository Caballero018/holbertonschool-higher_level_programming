#!/usr/bin/node
const myVar = process.argv;
let message;

if (Object.keys(myVar).length > 2) {
  message = 'Argument found';
  console.log(message);
} else {
  message = 'No argument';
  console.log(message);
}
