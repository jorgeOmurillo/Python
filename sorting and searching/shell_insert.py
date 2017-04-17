def shellSort(lista):

    sublist = len(lista) // 2
    
    while sublist > 0:

        for startpos in range(sublist):
            gapInsertSort(lista, startpos, sublist)

            print "Size increments", sublist, "the list is", lista
        
        sublist = sublist // 2


def gapInsertSort(lista, start, gap):

    for i in range(start + gap, len(lista), gap):

        currentValue = lista[i]
        pos = i

        while pos >= gap and lista[pos-gap] > currentValue:
            lista[pos] = lista[pos - gap]
            pos = pos - gap
        
        lista[pos] = currentValue

lista = [3567, 42, 6247, 6712, 22, 7]
shellSort(lista)

print lista
