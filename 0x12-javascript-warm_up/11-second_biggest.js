#!/usr/bin/node

let argv = process.argv;
if (argv.length < 4) { console.log(0); } else {
  argv = argv.slice(2);

  let num = argv.map(m => parseInt(m));
  num = num.sort(function (a, b) { return a - b; });
  console.log(num[num.length - 2]);
}
