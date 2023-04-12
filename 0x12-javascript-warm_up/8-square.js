#!/usr/bin/node
let i = 0;
let j = 0;
let string = '';
let firstArg = process.argv[2];
firstArg = parseInt(firstArg);
if (!isNaN(firstArg)) {
  while (i < firstArg) {
    while (j < firstArg) {
      string = string + 'X';
      j++;
    }
    console.log(string);
    i++;
  }
} else { console.log('Missing size'); }
