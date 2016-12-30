from pythonds.basic.stack import Stack

rStack = Stack()

def toSrt(n, base):

    convertString = "0123456789ABCDEF"

    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n % base])

        n = n//base

    res = ""

    while not rStack.isEmpty():
        res = res + str(rStack.pop())
    
    return res

print toSrt(1453, 16)
