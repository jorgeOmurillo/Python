def solution(n):
    arr = [0]*(n+1)
    arr[0], arr[1] = 0, 1

    for x in range(2, n+1):
        arr[x] = arr[x-1] + arr[x-2]

    return arr

print(solution(10))
