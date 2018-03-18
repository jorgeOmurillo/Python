import bisect

def solution(n):

    fib = [0,1]

    for x in range(2,60):
        fib.append(fib[x-1] + fib[x-2])
    
    res = []
    
    for y in n:
        res.append(fib[bisect.bisect_right(fib, y)])

    return res

print(solution([1,9,22]))
