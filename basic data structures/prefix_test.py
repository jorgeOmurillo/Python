from pythonds.basic.stack import Stack

def infixToPrefix(infixexpr):

    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opStack = Stack()
    preFixList = []
    tokenList = reverseText(infixexpr)

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            preFixList.append(token)
        
        elif token == ')':
            opStack.push(token)
        
        elif token == '(':
            topToken = opStack.pop()

            while topToken != '(':
                right = operandStack.pop()
                left = operandStack.pop()
                postFixList = postFixList + topToken + left + right
                topToken = opStack.pop()
 
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                #operandStack.push(opStack.pop())
                postFixList = opStack.pop() + postFixList
            opStack.push(token)

    while not opStack.isEmpty():
        while not operandStack.isEmpty():
            right = operandStack.pop()
            left = operandStack.pop()
            postFixList = opStack.pop() + left + right + postFixList

        postFixList = opStack.pop() + postFixList

    print postFixList


def reverseText(text):
    newText = Stack()
    for x in text:
        newText.push(x)

    result = ""

    for x in text:
        result += newText.pop()

    return result


infixToPrefix("( A + B ) * ( C + D )")
infixToPrefix("( A + B ) + ( C * D )")
infixToPrefix("5 * 3 ^ ( 4 - 2 )")
#infixToPrefix("8 / 9 ^ 7 * ( 9 - 1 )")
#infixToPrefix("A + ( ( B + C ) * ( D + E ) )")

infixToPrefix("( A + B ) * ( C + D ) * ( E + F )")
#infixToPrefix("A + ( ( B + C ) * ( D + E ) )")
infixToPrefix("A * B * C * D + E + F")
