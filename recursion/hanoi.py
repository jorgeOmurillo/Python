from pythonds.basic.stack import Stack

fromP = Stack()
toP = Stack()
withP = Stack()

def moveTower(height, fromPole, toPole, withPole):

    if height >= 1:
        moveTower(height-1, fromPole, withPole, toPole)
        fromP.push(fromPole)
        toP.push(toPole)
        withP.push(withPole)

        moveDisk(fromPole, toPole)
        toP.push(fromP.pop())

        moveTower(height-1, withPole, toPole, fromPole)

def moveDisk(fp, tp):
    print "moving disk from", fp, "to", tp

def printTower():
    while not toP.isEmpty():
        print toP.pop()

moveTower(3, "A", "B", "C")
printTower()
