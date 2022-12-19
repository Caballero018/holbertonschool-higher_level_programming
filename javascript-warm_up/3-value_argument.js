#!/usr/bin/node
const myVar = process.argv;
let message;

let i = 0
for (const arg in Object.keys(myVar)){
  i += 1
}

let len_myvar = i;
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
