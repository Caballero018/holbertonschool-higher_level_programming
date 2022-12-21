#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const ls of list) {
    if (ls === searchElement) {
      count++;
    }
  }
  return count;
};
