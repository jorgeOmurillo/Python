def factThis(num):
    
    if num == 0:
        return 1
    else:
        return num * factThis(num-1)

print factThis(5)
