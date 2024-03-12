#!/usr/bin/node

const PrevSquare = require('./5-square');

class Square extends PrevSquare {
  charPrint (c = 'X') {
    let squareStr = '';
    for (let i = 0; i < this.height; i++) {
      squareStr += c.repeat(this.width);
      if (i < this.height - 1) {
        squareStr += '\n';
      }
    }
    console.log(squareStr);
  }
}

module.exports = Square;
