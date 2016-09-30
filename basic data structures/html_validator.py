from pythonds.basic.stack import Stack

def htmlVal(htmlText):

    signStack = Stack()
    newText = list(htmlText)
    resultText = []

    for token in newText:

        if token == '<':
            resultText.append(token)
            signStack.push(token)

        elif token == '>':
            
            temp = signStack.pop()

            while temp != '<':
                
