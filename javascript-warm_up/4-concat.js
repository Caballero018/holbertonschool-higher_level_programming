#!/usr/bin/node
const args = process.argv;
let message;
let len = Object.keys(args).length;

if (len === 3) {
    message = `${args[2]} is undefined`
    console.log(message);
} else if (len === 4) {
    message = `${args[2]} is ${args[3]}`
    console.log(message);
} else {
    message = 'undefined is undefined';
    console.log(message);
}
