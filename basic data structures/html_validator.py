from pythonds.basic.stack import Stack

def htmlVal(htmlText):

    signStack = Stack()
    newText = list(htmlText)

    for token in newText:

        if token == '<':
            signStack.push(token)

        elif token == '>':
            signStack.pop()
