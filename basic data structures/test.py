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
    postFixList = []
    tokenList = reverseText(infixexpr.split())
    
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postFixList.append(token)
        
        elif token == ')':
            opStack.push(token)
        
        elif token == '(':
            topToken = opStack.pop()
            while topToken != ')':
                postFixList.append(topToken)
                topToken = opStack.pop()
 
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postFixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postFixList.append(opStack.pop())

    return " ".join(reverseText(postFixList))
 

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
