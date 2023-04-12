#!/usr/bin/node
let i = 0;
let firstArg = process.argv[2];
firstArg = parseInt(firstArg);
if (!isNaN(firstArg)) {
  while (i < firstArg) {
    console.log('C is fun');
    i++;
  }
} else { console.log('Missing number of occurrences'); }
