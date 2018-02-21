# def fibMe(num):

    # if num == 1:
        # return 1
    # elif num == 0:
        # return 0
    # else:
        # return fibMe(num-1) + fibMe(num-2)

# for i in range(10):
    # print(fibMe(i))

def getFib(n):
    a = 0
    b = 1
    
    for i in range(0, n):
        temp = a
        a = b
        b = temp + b
    return a

fibSorted = []

for c in range(0, 10):
    fibSorted.append(getFib(c))

def nextFibonacci(n):
    for x in n:
        for i in range(1, len(fibSorted)):
            if x == fibSorted[i]:
                print(x)
            else:
                if x > fibSorted[i] and x < fibSorted[i+1]:
                    print(fibSorted[i+1])

listMe = [6, 9, 33]
nextFibonacci(listMe)
