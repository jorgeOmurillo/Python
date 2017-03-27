def searchMe(listMe, num):

    found = False
    stop = False
    pos = 0

    while pos < len(listMe) and not found and not stop:

        if listMe[pos] == num:
            print listMe[pos]
            found = True
        else:
            if listMe[pos] > num:
                stop = True
            else:
                pos += 1

    return found

print searchMe([12, 1234, 2441, 232541], 2441)
