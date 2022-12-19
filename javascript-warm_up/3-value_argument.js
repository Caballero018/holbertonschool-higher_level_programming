#!/usr/bin/node
const myVar = process.argv;
let message;

function len(args){
    let i = 0
  for (const arg in args){
    i += 1
  }
  return i;
}

let len_myvar = len(Object.keys(myVar));
if (len_myvar >= 2) {
  let i = 2
  while (i < len_myvar){
    console.log(myVar[i]);
    i++
  }
} else {
  message = 'No argument';
  console.log(message);
}
