def quick_sort(A):
    quick_sort_helper(A, 0, len(A)-1)
    
    return A

def quick_sort_helper(A, first, last):
    if first < last:
        split = partition(A, first, last)

        quick_sort_helper(A, first, split-1)
        quick_sort_helper(A, split+1, last)


def partition(A, first, last): 
    pivot = A[first]

    left = first+1
    right = last

    done = False

    while not done:
        
        while left <= right and A[left] <= pivot:
            left += 1

        while right >= left and A[right] >= pivot:
            right -= 1

        if right < left:
            done = True
        else:
            temp = A[left]
            A[left] = A[right]
            A[right] = temp

    temp = A[first]
    A[first] = A[right]
    A[right] = temp

    return right

print(quick_sort([123,6,99,1,3,89,1233]))
