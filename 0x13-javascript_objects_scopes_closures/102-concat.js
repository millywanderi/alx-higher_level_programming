#!/usr/bin/node

const fs = require('fs');
const fileA = process.argv[2];
const fileB = process.argv[3];

const contentA = fs.readFileSync(fileA);
const contentB = fs.readFileSync(fileB);

const newContent = contentA + contentB;

fs.writeFile(process.argv[4], newContent, 'utf-8', (err) => {
  if (err) {
    throw err;
  }
});
