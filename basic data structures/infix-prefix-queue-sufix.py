from pythonds.basic.stack import Stack
from pythonds.basic.deque import Deque

def infixToPostfix(infixexpr):
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opStack = Stack()
    postFixList = Deque()
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postFixList.addRear(token)
        
        elif token == '(':
            opStack.push(token)
        
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postFixList.addRear(topToken)
                topToken = opStack.pop()
 
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postFixList.addRear(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postFixList.addRear(opStack.pop())

    newList = []
    while not postFixList.isEmpty():
        newList += postFixList.removeRear()

    return " ".join(newList)

print infixToPostfix("( A + B ) + ( C * D )")
print infixToPostfix("5 * 3 ^ ( 4 - 2 )")
