def sequential_search(valor):
    lista = [1,2,3,4,5,6,7]
    count = 0
    found = False

    while not found and count < len(lista):
        if lista[count] == valor:
            found = True
        else:
            count += 1

    return found

print(sequential_search(0))


def sequential_search_two(value):
    lista = [1,2,3,4,5,6,7,8]

    if value <= len(lista) and lista[value-1] == value:
        return True

    return False

print(sequential_search_two(1))
