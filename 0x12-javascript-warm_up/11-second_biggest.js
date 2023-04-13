#!/usr/bin/node
const sortedArray = [];
let i = 2;
let count = process.argv.length - 2;
if (count === 0 || count === 1) {
  console.log('0');
} else {
  while (count) {
    sortedArray.push(parseInt(process.argv[i]));
    i++;
    count--;
  }
  sortedArray.sort((a, b) => b - a);
  console.log((sortedArray[1]));
}
