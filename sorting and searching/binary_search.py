def binarySearch(listMe, num):
    first = 0
    last = len(listMe)-1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2

        if listMe[midpoint] == num:
            found = True
        else:
            if num < listMe[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found

print binarySearch([1,2,3,4,5,6,7,7,8], 7)
