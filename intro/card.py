""" Blackjack Game"""

import random

class Card:

    def __init__(self):
        self.res = generateDeck()

    def __str__(self):
        return '{}'.format(self.res)

    def drawOne(self):

        self.pickMe = drawCard(self.res)

        return self.pickMe


def drawCard(deck):
    random.shuffle(deck)

    return [deck.pop() for k in range(1)]


def generateDeck():

    deck = []

    for rank in 'A23456789TJQK':
        for suit in 'CDHS':
            deck = deck + [rank+suit]

    return deck


def main():

    cardDeck = Card()
    count = 0

    while count <= 21:
        response = raw_input("Press a key to draw a card.\n")
        temp = cardDeck.drawOne()

        if temp[0][0] == 'A':
            other = 1
        elif temp[0][0] == 'T':
            other = 10
        elif temp[0][0] == 'J':
            other = 11
        elif temp[0][0] == 'Q':
            other = 12
        elif temp[0][0] == 'K':
            other = 13
        else:
            other = int(temp[0][0])


        count += other

        print "You drew a " + temp[0][0] + " of " + temp[0][1] + ". You have a total of: " + str(count) + ".\n" 

        if count == 21:
            print "You won! 21 Blackjack. Your total count is: " + str(count)
            break
        if count > 21:
            print "You lost!"
            break
        
if __name__ == "__main__":
    main()
