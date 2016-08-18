from __future__ import division
import random

text = 'methinks it is like a weasel'

def generate_string(length):
    alpha = 'abcdefghijklmnopqrstuvwxyz '
    result = ''

    for x in range(length):
        result = result + alpha[random.randrange(27)]

    return result

def score(goal, test_string):
    numSame = 0
    for i in range(len(goal)):
        if goal[i] == test_string[i]:
            numSame += 1

    ans = numSame/len(goal)

    return ans

def findText():
    newString = generate_string(28)
    bestScore = 0
    newScore = score(text, newString)
    divisible = 0

    while (newScore < 1):
        divisible += 1
        if (divisible % 1000000) == 0:
            print "Reached " + str(divisible) + " million."
            print "Best string: " + newString
        if (newScore >= bestScore):
            print newScore, newString
            bestScore = newScore
        newString = generate_string(28)
        newScore = score(text, newString)

def foundText():
    newString = generate_string(28)
    newList = ""
    found = False
    count = 0

    while found == False and count != 28:
        if newList == newString:
            found = True
            continue
        if (newString[count] != text[count]):
            print count
            newString = generate_string(28)
        if (newString[count] == text[count]):
            newList = newList + newString[count]
            count += 1

    print newList

foundText()
findText()
