""" Blackjack Game"""

import random

class Card:

    def __init__(self):
        self.res = generateDeck()

    def __str__(self):
        return '{}'.format(self.res)

    def draw(self):

        self.pickMe = drawCard(1, self.res)
        self.selected = self.pickMe[0][0]

        if self.selected == 'A':
            self.selected = 1
        elif self.selected == 'T':
            self.selected = 10
        elif self.selected == 'J':
            self.selected = 11
        elif self.selected == 'Q':
            self.selected = 12
        elif self.selected == 'K':
            self.selected = 13
        else:
            self.selected = int(self.selected)

        return int(self.selected)


def drawCard(n, deck):
    random.shuffle(deck)

    return [deck.pop() for k in range(n)]


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
    
        count += cardDeck.draw()

        print count

        if count == 21:
            print "You won! 21 Blackjack."
            break
        if count > 21:
            print "You lost :( !"
            break
        
if __name__ == "__main__":
    main()
