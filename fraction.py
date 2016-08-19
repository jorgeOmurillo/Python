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
        secondnum = self.num * self.den

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
        
def gcd(m, n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn

    return n

#myFraction = Fraction(3, 5)

#print "I ate", myFraction, "of the pizza"
#print myFraction.__str__()

f1 = Fraction(1, 3)
f2 = Fraction(4,7)
f3 = f1+f2

print f3

f4 = f1-f2

print f4
