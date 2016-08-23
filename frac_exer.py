from __future__ import division

class Fraction:

    def __init__(self, n, d):
        self.n = n
        self.d = d
        self.common = gcd(self.n, self.d)

    def __str__(self):
        return str(self.n//self.common) + "/" + str(self.d//self.common)

    def __add__(self, secFrac):
        newNum = self.n * secFrac.d + self.d * secFrac.n
        newDen = self.d * secFrac.d

        return Fraction(newNum//self.common, newDen//self.common)

    def __radd__(self, secFrac):
        if secFrac == 0:
            return self
        else:
            return self.__add__(secFrac)

    def __iadd__(self, secFrac):
        num1 = self.n * secFrac.d
        num2 = self.d * secFrac.n
        num1 += num2

        return num1

    def __sub__(self, secFrac):
        newNum = self.n * secFrac.d - self.d * secFrac.n
        newDen = self.d * secFrac.d
        
        return Fraction(newNum//self.common, newDen//self.common)
    
    def __mul__(self, secFrac):
        newNum = self.n * secFrac.n
        newDen = self.d * secFrac.d

        return Fraction(newNum//self.common, newDen//self.common)

    def __truediv__(self, secFrac):
        newNum = self.n * secFrac.d
        newDen = self.d * secFrac.n

        return Fraction(newNum//self.common, newDen//self.common)

    def __gt__(self, secFrac):
        num1 = self.n * secFrac.d
        num2 = self.d * secFrac.n

        return num1 > num2

    def __ge__(self, secFrac):
        num1 = self.n * secFrac.d
        num2 = self.d * secFrac.n

        return num1 >= num2

    def __lt__(self, secFrac):
        num1 = self.n * secFrac.d
        num2 = self.d * secFrac.n

        return num1 < num2

    def __le__(self, secFrac):
        num1 = self.n * secFrac.d
        num2 = self.d * secFrac.n

        return num1 <= num2

    def __ne__(self, secFrac):
        num1 = self.n * secFrac.d
        num2 = self.d * secFrac.n

        return num1 != num2

    def getNum(self):
        return self.n//self.common

    def getDen(self):
        return self.d//self.common

def gcd(num, den):

    while num%den != 0:
        oldNum = num
        oldDen = den

        num = oldDen
        den = oldNum%oldDen

    return den

f1 = Fraction(2, 8)
f2 = Fraction(2, 6)

f1 += f2

print f1+f2, f1-f2, f1*f2, f1/f2, f1>f2, f1>=f2, f1<f2, f1<=f1, f1!=f2
print "Sum ", f1
