from __future__ import division

class Fraction:
    
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)

        return Fraction(newnum//common, newden//common)
    
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        common = gcd(firstnum, secondnum)

        return firstnum == secondnum

    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)

        return Fraction(newnum//common, newden//common)

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        common = gcd(newnum, newden)

        return Fraction(newnum//common, newden//common)

    def __lt__(self, other):
        firstNum = self.num * other.den
        secondNum = self.den * other.num

        return firstNum < secondNum

    def __gt__(self, other):
        firstNum = self.num * other.den
        secondNum = self.den * other.num

        return firstNum > secondNum

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den    

 
def gcd(m, n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn

    return n

f = Fraction(1, 3)
g = Fraction(1, 6)

k = f+g

print "Addition: ", k

print "Substraction: ", f-g

print "Division: ", f/g

print "Multiplication: ", f*g

print "Less than: ", f<g 

print "Greater than: ", f>g

print "Equal: ", f==g
