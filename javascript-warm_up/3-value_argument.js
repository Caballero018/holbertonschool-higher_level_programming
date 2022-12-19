#!/usr/bin/node
const myVar = process.argv;
let message;
let lenmyvar = 0;
let i;

// eslint-disable-next-line no-unused-vars
for (const arg in myVar) {
  lenmyvar += 1;
}

if (lenmyvar > 2) {
  i = 2;
  while (i < lenmyvar) {
    console.log(myVar[i]);
    i++;
  }
} else {
  message = 'No argument';
  console.log(message);
}
