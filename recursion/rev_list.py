def revList(thisList):

    if len(thisList) == 1:
        return thisList
    else:
        return thisList[-1:] + revList(thisList[:-1])


myList = [1,2,3,4,5]

print revList(myList)
