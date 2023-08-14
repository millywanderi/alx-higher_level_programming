#!/usr/bin/node

const fun = 'C is fun';

if (process.argv.length >= 3) {
  let m = process.argv[2];
  while (m > 0) {
    console.log(fun);
    m--;
  }
} else {
  console.log('Missing number of occurrences');
}
