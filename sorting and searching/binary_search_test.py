def solution(A, n):

    first = 0
    last = len(A)-1
    found = False

    while not found and first <= last:
        mid = (first+last)//2

        if A[mid] == n:
            found = True
        else:
            if A[mid] > n:
                last = mid-1
                print(A[mid])
            else:
                first = mid+1

    return found

print(solution([1,2,3,4,5],0))
