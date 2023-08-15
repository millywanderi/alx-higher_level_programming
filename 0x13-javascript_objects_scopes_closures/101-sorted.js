#!/usr/bin/node

const dict = require('./101-data.js');

const nDict = {};
const enti = dict.dict;

for (const key in enti) {
  if (nDict[enti[key]] === undefined) {
    nDict[enti[key]] = [key];
  } else {
    nDict[enti[key]].push(key);
  }
}
console.log(nDict);
