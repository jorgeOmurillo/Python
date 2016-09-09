#from __future__ import division

import time

def sumOfN2(n):
    start = time.time()

    sum = 0

    for i in range(1, n+1):
        sum += 1

    end = time.time()

    return sum, end - start


def sumOfN3(n):
    return (n*(n+1))/2

for i in range(5):
    print "Sum is %d required %10.7f seconds" % sumOfN2(10000000)

print sumOfN3(10)
