#!/usr/bin/node

function factorialFind (m) {
  if (m < 0) {
    return (-1);
  }
  if (m === 0 || isNaN(m)) {
    return (1);
  }
  return (m * factorialFind(m - 1));
}
console.log(factorialFind(Number(process.argv[2])));
