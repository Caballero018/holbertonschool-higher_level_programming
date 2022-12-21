#!/usr/bin/node
let count = -1;
exports.logMe = function (item) {
  count += 1;
  console.log(`${count}: ${item}`);
};
