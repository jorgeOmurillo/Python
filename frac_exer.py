class Fraction:

    def __init__(self, n, d):
        self.n = n
        self.d = d
        self.common = gcd(self.n, self.d)

    def __str__(self):
        return str(self.n//self.common) + "/" + str(self.d//self.common)

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

test = Fraction(2, 10)

print test
