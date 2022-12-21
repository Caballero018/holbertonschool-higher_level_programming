#!/usr/bin/node
const add = require('./5-square');
module.exports = class Square extends add {
  charPrint (c = 'X') {
    let ch;
    for (let i = 0; i <= this.width; i++) {
      ch = '';
      for (let j = 0; j <= this.width; j++) {
        ch += c;
      }
      console.log(ch);
    }
  }
};
