#!/usr/bin/node
const count = process.argv.length;

// Script that prints messages depending of the argument.

console.log(count === 2 ? 'No argument' : count === 3 ? 'Arguments found' : 'Arguments found');