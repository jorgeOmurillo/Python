def binaryMe(listMe, num):

    if len(listMe) == 0:
        return False
    else:

        mid = len(listMe)//2

        if listMe[mid] == num:
            return True
        else:
            if num < listMe[mid]:
                return binaryMe(listMe[:mid], num)
            else:
                return binaryMe(listMe[mid+1:], num)

esta = [1, 2, 3, 4, 5, 6]

print binaryMe(esta, 10)
