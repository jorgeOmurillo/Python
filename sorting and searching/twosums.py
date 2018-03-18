def solution(lista, target):
    res = {}

    for x in range(len(lista)):
        res[x] = lista[x]

    for y in range(len(lista)):
        resta = target - lista[y]

        if resta in res:
            return y, res[resta]

print(solution([2,11,7,15], 9))
print(solution([3,2,4], 6))
