from __future__ import division
from pythonds.basic.stack import Stack

def baseConverter(decNumber, base):

    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:

        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""

    while not remstack.isEmpty():
        newString += digits[remstack.pop()]

    return newString

print baseConverter(25, 8)
print baseConverter(26, 26)
