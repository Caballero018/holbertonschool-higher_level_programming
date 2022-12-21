#!/usr/bin/node
exports.esrever = function (list) {
  let i = Object.keys(list).length - 1;
  let j = 0;
  const change = [];
  const copy = [].concat(list);
  for (const ls of list) {
    change[j] = list[i];
    copy[i] = ls;
    i--;
    j++;
  }
  return copy;
};
