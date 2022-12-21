#!/usr/bin/node
const add = require('./5-square');
module.exports = class Square extends add {
  constructor (size) {
    super(size);
  }

  charPrint (c = 'X') {
    let ch;
    for (let i = 0; i <= this.size; i++) {
      ch = '';
      for (let j = 0; j <= this.size; j++) {
        ch += c;
      }
    console.log(ch);
    }
  }
};
