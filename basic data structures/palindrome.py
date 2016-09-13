from pythonds.basic.deque import Deque

def palChecker(text):

    check = Deque()

    for x in text:
        check.addRear(x)

    equal = True

    while check.size() > 1 and equal:
        first = check.removeFront()
        second = check.removeRear()

        if first != second:
            equal = False

    return equal

print palChecker("proba")
print palChecker("radar")
