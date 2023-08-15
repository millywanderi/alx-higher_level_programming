#!/usr/bin/node

const list = require('./100-data').list;

const aray = list.map((x, m) => x * m);

console.log(list);
console.log(aray);
