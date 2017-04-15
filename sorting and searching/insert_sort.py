def insertSort(lista):

    for index in range(1, len(lista)):

        currentValue = lista[index]
        position = index

        while position > 0 and lista[position - 1] > currentValue:

            lista[position] = lista[position - 1]
            position -= 1

        lista[position] = currentValue

lista = [23, 441, 1, 1231, 5]

insertSort(lista)

print lista
