class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def myString(self):
        self.reversed = reverseString(self)

        return self.reversed


def reverseString(text):

    testStack = Stack()

    for x in text:
        testStack.push(x)

    revStr = ''

    while not testStack.isEmpty():
        revStr += testStack.pop()

    return revStr

hello = reverseString('Jorge')

print hello
