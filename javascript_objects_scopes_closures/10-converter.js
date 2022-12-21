#!/usr/bin/node
exports.converter = function (base) {
  return function (bas) {
    return bas.toString(base);
  };
};
