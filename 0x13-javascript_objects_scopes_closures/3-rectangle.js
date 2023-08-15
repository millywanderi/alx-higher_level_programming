#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (((w = parseInt(w)) > 0) && ((h = parseInt(h)) > 0)) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    const rect = 'X'.repeat(this.width);
    for (let m = 0; m < this.height; m++) {
      console.log(rect);
    }
  }
}
module.exports = Rectangle;
