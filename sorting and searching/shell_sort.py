def shell_sort(A):

    gap = len(A) // 2

    while gap > 0:

        for x in range(gap):

            for y in range(x+gap, len(A), gap):
                current = A[y]
                index = y

                while index >= gap and A[index-gap] > current:
                    A[index] = A[index-gap]
                    index -= gap

                A[index] = current

        gap //= 2

    return A


print(shell_sort([468,89,223,900,2,1,7,36,8,9]))
