from pythonds.basic.stack import Stack

def infixToPrefix(infixexpr):
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec[")"] = 1

    opStack = Stack()
    preFixList = []
    tokenList = reverseText(infixexpr.split())
    
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            preFixList.append(token)
        
        elif token == ')':
            opStack.push(token)
        
        elif token == '(':
            topToken = opStack.pop()
            while topToken != ')':
                preFixList.append(topToken)
                topToken = opStack.pop()
 
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                preFixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        preFixList.append(opStack.pop())

    return " ".join(reverseText(preFixList))
 

def reverseText(text):
    newText = ""
    newStack = Stack()

    for x in text:
        newStack.push(x)

    for x in text:
        newText += newStack.pop()

    return newText

print infixToPrefix("( A + B ) * ( C + D )")
print infixToPrefix("( A + B ) * ( C + D ) * ( E + F )")
print infixToPrefix("A + ( ( B + C ) * ( D + E ) )")
print infixToPrefix("A * B * C * D + E + F")
