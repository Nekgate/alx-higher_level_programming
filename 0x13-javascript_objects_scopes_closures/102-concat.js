#!/usr/bin/node
const fs = require('fs');
const a = fs.readFileSync(process.arg[2], 'utf8');
const b = fs.readFileSync(process.arg[3], 'utf8');
fs.writeFileSync(process.arg[4], a + b);
