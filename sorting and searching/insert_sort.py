def insertSort(lista):

    for index in range(0, len(lista)):

            position = index
            currentValue = lista[index]

            while position > 0 and lista[position - 1] > currentValue:
                lista[position] = lista[position - 1]
                position -= 1

            lista[position] = currentValue

lista = [86752, 14, 1234, 1]
insertSort(lista)

print lista
