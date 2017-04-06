def bubbleS(lista):

    exchanges = True
    passnum = len(lista)-1

    while passnum > 0 and exchanges:
        exchanges = False

        for i in range(passnum):
            if lista[i] > lista[i+1]:
                exchanges = True
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
        passnum -= 1

lista = [100, 2123, 444, 111, 6123123]

bubbleS(lista)

print lista
