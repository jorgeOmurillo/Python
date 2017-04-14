def selectionSort(lista):

    for fillslot in range(len(lista)-1, 0, -1):
        maxPosition = 0

        for location in range(1, fillslot + 1):
            if lista[location] > lista[maxPosition]:
                maxPosition = location

        temp = lista[fillslot]
        lista[fillslot] = lista[maxPosition]
        lista[maxPosition] = temp

lista = [44, 221, 6, 112, 778, 12, 147]
selectionSort(lista)

print lista
