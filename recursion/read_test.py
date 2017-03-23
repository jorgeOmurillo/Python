textThis = open('sample.txt', 'r')
f = textThis.read()

myList = {}

for i in f:
    if i in myList:
        myList[i] += 1
    else:
        myList[i] = 1

print myList
