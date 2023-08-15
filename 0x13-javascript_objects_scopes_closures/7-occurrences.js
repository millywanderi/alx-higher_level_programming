#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let tally = 0;
  for (let m = 0; m < list.length; m++) {
    if (list[m] === searchElement) {
      tally++;
    }
  }
  return tally;
};
