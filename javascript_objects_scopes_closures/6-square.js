#!/usr/bin/node
const add = require('./5-square');
module.exports = class Square extends add {
  charPrint (c = 'X') {
    let ch;
    for (let i = 1; i <= this.width; i++) {
      ch = '';
      for (let j = 1; j <= this.width; j++) {
        ch += c;
      }
      console.log(ch);
    }
  }
};
