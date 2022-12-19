#!/usr/bin/node
const args = process.argv;
function factorial (a) {
  if (!(isNaN(a)) && Number(a) > 0) {
    return Number(a) * factorial(Number(a) - 1);
  } else {
    return 1;
  }
}
console.log(factorial(args[2]));
