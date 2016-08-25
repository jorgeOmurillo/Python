from random import randrange

class Card:

    def __init__(self):
        self.res = generateDeck()

    def __str__(self):
        return '{}'.format(self.res)

def generateCard():

    numberSel = number[randrange(0, len(number))]
    signSel = sign[randrange(0, len(sign))]

    #result =  number[randrange(0, len(number))] + " of " + sign[randrange(0, len(sign))]

    result = [numberSel[0], signSel[0]]

    return result

def generateDeck():

    deck = []

    for rank in 'A23456789TJQK':
        for suit in 'CDHS':
            deck = deck + [rank+suit]

    return deck

c1 = Card()

print c1
