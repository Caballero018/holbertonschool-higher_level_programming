#!/usr/bin/node
const args = process.argv;
function add (a, b) {
  const len = Object.keys(args).length;
  if (!(isNaN(parseInt(a)) || len === 3)) {
    return parseInt(a) + parseInt(b);
  } else {
    return NaN;
  }
}
console.log(add(args[2], args[3]));
