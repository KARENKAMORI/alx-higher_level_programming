#!/usr/bin/node

function factorial (number) {
  if (number > 0) {
    return number * factorial(number - 1);
  }
  return 1;
}

console.log(factorial(Number(process.argv[2])));
