def hashed(lista, N):
    arr = [None] * N

    for x in range(len(lista)):
        arr[lista[x]%N] = lista[x]

    return arr

print(hashed([54,26,93,17,77,31,31], 11))
