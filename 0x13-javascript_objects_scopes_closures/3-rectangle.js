#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (((w = parseInt(w)) > 0) && ((h = parseInt(h)) > 0)) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    for (let m = 0; m < this.height; m++) {
      let row = '';
      for (let n = 0; n < this.width; n++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}
module.exports = Rectangle;
