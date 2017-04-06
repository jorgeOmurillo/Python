def binarySearch(listMe, num):
    if len(listMe) == 0:
        return False
    else:
        midpoint = len(listMe)//2

        if listMe[midpoint] == num:
            return True
        else:
            if num < listMe[midpoint]:
                return binarySearch(listMe[:midpoint], num)
            else:
                return binarySearch(listMe[midpoint+1:], num)

print binarySearch([1,2,3,4,5,6,7,8,6,10], 11)
