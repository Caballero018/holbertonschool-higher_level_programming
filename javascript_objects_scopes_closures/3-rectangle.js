#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !w || !h) {
      return this;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let x;
    for (let i = 1; i <= this.height; i++) {
      x = '';
      for (let j = 1; j <= this.width; j++) {
        x += 'X';
      }
      console.log(x);
    }
  }
};
