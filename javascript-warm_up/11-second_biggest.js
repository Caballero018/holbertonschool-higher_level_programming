#!/usr/bin/node
const args = process.argv;
const len = Object.keys(args).length;

function second_max (array) {
  const ar = [].concat(array);
  const ar2 = [].concat(array);
  let i;

  for (i = 4; i <= Object.keys(array).length; i++) {
    if (Number(ar[2]) < Number(array[i])) {
      ar[2] = array[i];
    }
    i++;
  }
  for (i = 4; i <= Object.keys(array).length; ++i) {
    if (Number(ar2[2]) < Number(array[i]) && Number(ar2[2]) < Number(ar[2])) {
      ar2[2] = array[i];
    }
  }
  return ar2[2];
}

if (len > 3) {
  console.log(second_max(args));
} else {
  console.log(1);
}
