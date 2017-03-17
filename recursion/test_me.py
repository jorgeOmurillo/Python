source = [4,3,2,1]
helper = []
target = []

def hanoi(height, source, helper, target):

    if height > 0:
        hanoi(height-1, source, target, helper)

        target.append(source.pop())

        hanoi(height-1, helper, source, target)

hanoi(4, source, helper, target)

print target
