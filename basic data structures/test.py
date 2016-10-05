from pythonds.basic.stack import Stack

def testStack():

    textStack = Stack()

    thisWord = "hola"

    for x in thisWord:
        textStack.push(x)

    print textStack.peek()


testStack()
