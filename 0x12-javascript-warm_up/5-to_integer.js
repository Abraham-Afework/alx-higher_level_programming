#!/usr/bin/node
const myNumber = 1;
const firstArg = process.argv[2];
if (typeof (firstArg * myNumber) === 'number') {
  console.log('My Number: ' + firstArg);
} else { console.log('Not a number'); }
