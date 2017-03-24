def fibMe(num):

    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibMe(num-1) + fibMe(num-2)

print fibMe(5)
