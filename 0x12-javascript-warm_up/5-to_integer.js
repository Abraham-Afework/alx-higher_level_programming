#!/usr/bin/node

let firstArg = process.argv[2];

firstArg = parseInt(firstArg);

if (!isNaN(firstArg)) {
  console.log('My number: ' + firstArg);
} else { console.log('Not a number'); }
