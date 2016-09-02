from pythonds.basic.stack import Stack

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            
            result = doMath(token, operand1, operand2)
            operandStack.push(result)

    return operandStack.pop()

def doMath(one, two, three):

    if one == "*":
        return two * three
    
    elif one == "/":
        return two / three

    elif one == "+":
        return two + three

    else:
        return two - three

print postfixEval("6 8 + 7 6 +")
