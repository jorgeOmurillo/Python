def bubbleSort(listMe):

    for i in range(len(listMe)-1, 0, -1):
        for j in range(i):

            if listMe[j] > listMe[j+1]:
                temp = listMe[j]
                listMe[j] = listMe[j+1]
                listMe[j+1] = temp

listMe = [54, 26, 93, 17, 77, 31, 44, 55, 20]

bubbleSort(listMe)

print listMe
