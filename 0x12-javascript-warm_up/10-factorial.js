#!/usr/bin/node

const m = parseInt(process.argv[2]);

function factorialFind (m) {
  if (!m) { return 1; }

  if (m <= 0) { return; }
  return factorialFind(m - 1) * m;
}
console.log(factorialFind(m));
