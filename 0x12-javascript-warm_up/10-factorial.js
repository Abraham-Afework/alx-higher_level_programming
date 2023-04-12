#!/usr/bin/nodejs
function factorial (a) {
  if (a === 1) {
    return 1;
  }
  return a * factorial(a - 1);
}
const firstArg = parseInt(process.argv[2]);
if (isNaN(firstArg)) {
  console.log('1');
} else {
  console.log(factorial(firstArg));
}
