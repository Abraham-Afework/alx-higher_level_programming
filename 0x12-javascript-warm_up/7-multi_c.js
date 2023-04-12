#!/usr/bin/node
const myNumber = 1;
let i = 0;
const firstArg = process.argv[2];
console.log(typeof(firstArg - myNumber));
if (typeof(firstArg * myNumber) == 'number') {
  while (i < firstArg){
  console.log('C is fun');
  i++;
  }

} else { console.log('Missing number of occurrences'); }
