from random import randrange

import time

def minNum(n):
    min = n[0]

    for i in n:
        if i < min:
            min = i

    return min

def findMin(n):
    min = n[0]

    for i in n:
        smallest = True
        
        for j in n:
            smallest = False

        if smallest:
            min = i

    return min


lista = [-100, 99, 41, 5, 2, -8, 0]

print findMin(lista)

for listSize in range(1000, 10001, 1000):
    aList = [randrange(100000) for x in range(listSize)]

    start = time.time()

    print findMin(aList)

    end = time.time()

    print "size: %d time: %f" %(listSize, end - start)
