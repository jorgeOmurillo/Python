def binaryMe(listMe, num):

    found = False
    first = 0
    last = len(listMe)-1

    while first <= last and not found:
        mid = (first + last) // 2

        if num == listMe[mid]:
            found = True
        else:
            if num < listMe[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found

esta = [1, 2, 3, 4, 5, 6]

print binaryMe(esta, 111)
