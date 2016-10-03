from pythonds.basic.stack import Stack

def htmlVal(htmlText):

    carStack = Stack()
    newText = list(htmlText)
    resultText = ""
    beginning = False
    end = False

    for token in newText:

        if token == '<':
            beginning = True
            carStack.push(token)

        elif token == '>' and not end:
            beginning = False
            carStack.push(token)

        elif token in 'abcdefghijklmnopqrstuvwxyz12345' and beginning:
            carStack.push(token)

        elif token == '/':
            end = True
            carStack.push(token)

        else:
            if token == '>' and end:
                word2 = ""
                temp = carStack.pop()

                while temp != '/':
                    word2 = temp + word2
                    temp = carStack.pop()

                temp = carStack.pop()
                temp = carStack.pop()
                temp = carStack.pop()

                word1 = ""

                while temp != '<':
                    word1 = temp + word1
                    temp = carStack.pop()

                if word1 == word2:
                    print "Tags are complete: ", word1, word2
                else:
                    print "Tags are incomplete: ", word1, word2

            end = False

    return resultText

print htmlVal("<html><head><title>Example</title></head><body><h1>Hello, world</h1></body></html>")
