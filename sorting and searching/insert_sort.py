def insert_sort(A):
    
    for x in range(1, len(A)):
        current = A[x]
        index = x

        while index > 0 and A[index-1] > current:
            A[index] = A[index-1]
            index -= 1

        A[index] = current

    return A

print(insert_sort([78,89,123,2,5,9,1]))
