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

                """temp = carStack.pop()
                temp = carStack.pop()
                temp = carStack.pop()"""

                word1 = ""
<<<<<<< HEAD
                found = False

                #while temp != '<':
                while not found:
                    if temp == '>':
                        temp = carStack.pop()
                    while temp != '<':
                        word1 = temp + word1
                        temp = carStack.pop()

                    #temp = carStack.pop()

                    if word1 != word2:
                        print "This tag is incomplete: ", word1
                    else:
                        found = True
                        #print "Tags are incomplete: ", word1, word2
=======

                while temp != '<':
                    word1 = temp + word1
                    temp = carStack.pop()

                if word1 != word2:
                    print "This tag is incomplete: ", word1

                    for x in word2:
                        carStack.push(x)

                else:
                    print "Tags are complete: ", word1
>>>>>>> a2c3f566e253a53b53a5cc2b0f62bdc8b0be6ab7

            end = False

    return resultText

print htmlVal("<html><head><title>Example</head><body><h1>Hello, world</h1></body></html>")
