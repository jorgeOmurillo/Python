class BinaryTree:
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None

    def insertLeft(self, newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t

    def insertRight(self, newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t

    def getLeft(self):
        return self.left.key

    def getRight(self):
        return self.right.key

    def setRootVal(self, val):
        self.key = val

    def getRootVal(self):
        return self.key

test = BinaryTree(6)
test.insertLeft(5)
test.insertRight(77)

print(test.getLeft(), test.getRight())
