class ListOfList:
    def __init__(self, r):
        self.r = [r, [], []]

    def print_list(self):
        return self.r

    def insertLeft(self, newBranch):
        t = self.r.pop(1)

        if len(t) > 1:
            self.r.insert(1, [newBranch, t, []])
        else:
            self.r.insert(1, [newBranch, [], []])

    def insertRight(self, newBranch):
        t = self.r.pop(2)

        if len(t) > 1:
            self.r.insert(2, [newBranch, t, []])
        else:
            self.r.insert(2, [newBranch, t, []])

    def getRootVal(self):
        return self.r[0]

    def setRootVal(self, x):
        self.r[0] = x

    def getLeftChild(self):
        return self.r[1]

    def getRightChild(self):
        return self.r[2]

test = ListOfList(3)

test.insertLeft(4)
test.insertRight(5)
test.insertRight(6)
test.insertRight(7)

l = test.getLeftChild()

print(l)

test.setRootVal(9)
print(test.print_list())

test.insertLeft(11)
print(test.print_list())

print(test.getRightChild())
