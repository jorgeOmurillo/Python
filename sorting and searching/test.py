def binaryMe(lista, num, first, last):

    mid = (first + last) // 2

    if last <= first:
        return False
    else:
        if lista[mid] == num:
            return True
        else:
            if lista[mid] > num:
                return binaryMe(lista, num, first, mid)
            else:
                return binaryMe(lista, num, mid+1, last)

lista = [1,2,3,4,5,6,7]
print binaryMe(lista, 8, 0, len(lista))
