"use strict";

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

x1 = 0;
var x2 = 2;

function sum(a, b) {
  return a + b;
}

var test = function test(x1, x2) {
  _classCallCheck(this, test);

  this.x1 = x1;
  this.x2 = x2;
};

sum_result = sum(x1, x2);
console.log("The sum is: " + sum_result);
