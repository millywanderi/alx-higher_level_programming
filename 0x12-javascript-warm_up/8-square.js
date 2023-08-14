#!/usr/bin/node

const size = process.argv[2];

if (size && parseInt(size)) {
  let m = 0;
  while (m < size) {
    const x = 'X'.repeat(size);
    console.log(x);
    m++;
  }
} else {
  console.log('Missing size');
}
