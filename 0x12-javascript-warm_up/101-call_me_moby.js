#!/usr/bin/node

exports.callMeMoby = function (x, thefunction) {
  let i = 0;
  while (i < x) {
    thefunction();
    i++;
  }
};
