#!/usr/bin/node
const list = require('./100-data').list;
const newArray = list.map((element, index) => element * index);
console.log(list);
console.log(newArray);
