""" Blackjack Game"""

import random

class Card:

    def __init__(self):
        self.res = generateDeck()

    def __str__(self):
        return '{}'.format(self.res)

    def draw(self):

        self.pickMe = drawCard(1, self.res)
        self.pickMe = self.pickMe[0][0]

        if self.pickMe == 'A':
            self.pickMe = 1
        elif self.pickMe == 'T':
            self.pickMe = 10
        elif self.pickMe == 'J':
            self.pickMe = 11
        elif self.pickMe == 'Q':
            self.pickMe == 12
        elif self.pickMe == 'K':
            self.pickMe = 13
        else:
            self.pickMe = int(self.pickMe)

        print self.pickMe

        return self.pickMe


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


if __name__ == "__main__":
    main()
