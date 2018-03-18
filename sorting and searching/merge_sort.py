def merge_sort(A):
    mid = (0 + len(A)) // 2

    if len(A) > 1:
        left = []
        right = []

        for x in range(mid):
            left.append(A[x])

        for y in range(mid, len(A)):
            right.append(A[y])

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1

    return A

print(merge_sort([67,89,2,83,178,31,13,9,1,23]))
