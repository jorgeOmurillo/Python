def searchThis(listMe, item):
    pos = 0
    found = False

    while pos < len(listMe) and not found:
        if listMe[pos] == item:
            found = True
        else:
            pos += 1

    return found

thisList = [1,2,3,4,5,6,7,8]
print searchThis(thisList, 10)
print searchThis(thisList,8)
