from random import randrange

class Card:

    def __init__(self):
        self.res = generateCard()

    def __str__(self):
        return self.res

    

def generateCard():
    #sign = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
    sign = ['C', 'S', 'D', 'H']    
    #number = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]    

    #result =  number[randrange(0, len(number))] + " of " + sign[randrange(0, len(sign))]
    result = int(number(randrange(0, len(number)))) + int(sign(randrange(0, len(sign))))

    return result

c1 = Card()

print c1
