#!/usr/bin/node
const args = process.argv;
const len = Object.keys(args).length;

function findSecondLargestElem (arr) {
  let first = -1;
  let second = -1;

  for (let i = 0; i <= Object.keys(arr).length - 1; i++) {
    if (Number(arr[i]) > first) {
      second = first;
      first = arr[i];
    } else if (Number(arr[i]) > second && Number(arr[i]) !== first) {
      second = arr[i];
    }
  }
  console.log(second);
}

if (len > 3) {
  findSecondLargestElem(args);
} else {
  console.log(0);
}
