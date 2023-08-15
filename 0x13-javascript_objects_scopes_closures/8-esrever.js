#!/usr/bin/node

exports.esrever = function (list) {
  const lists = [];
  for (let m = list.length - 1; m >= 0; m--) {
    lists.push(list[m]);
  }
  return lists;
};
