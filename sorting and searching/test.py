def binary_search(lista, value):
    first = 0
    last = len(lista)-1
    found = False
    mid = (first + last) //2

    while not found and first <= last:
        if lista[mid] == value:
            found = True
            return found
        else:
            if value < lista[mid]:
                last = mid-1
                mid = (first + last) // 2
            else:
                first = mid+1
                mid = (first + last) // 2

    return found

# print(binary_search([1,2,3,4,5,6], 0))

def binary_search_recur(lista, value):
    mid = (len(lista)-1)//2

    if mid < 0:
        return False
    elif lista[mid] == value:
        return True
    else:
        if value > lista[mid]:
            return binary_search_recur(lista[mid+1:], value)
        else:
            return binary_search_recur(lista[:mid], value)

    return False

print(binary_search_recur([-1,0,1,2,3,4,5,6,7], -1))
print(binary_search_recur([1,2,3,4,5,6,7], 1))
print(binary_search_recur([1,2,3,4,5,6,7], 7))
print(binary_search_recur([1,2,3,4,5,6,7], 8))

def binary_search_recur_two(lista, value):
    if len(lista) == 0:
        return False
    else:
        mid = len(lista) // 2

        if lista[mid] == value:
            return True
        else:
            if value < lista[mid]:
                return binary_search_recur_two(lista[:mid], value)
            else:
                return binary_search_recur_two(lista[mid+1:], value)

<<<<<<< HEAD
# print(binary_search_recur_two([-1,0,1,2,3,4,5,6,7], -1))
# print(binary_search_recur_two([1,2,3,4,5,6,7], 1))
# print(binary_search_recur_two([1,2,3,4,5,6,7], 7))
# print(binary_search_recur_two([1,2,3,4,5,6,7], 8))
=======
lista = [1,2,3,4,5,6,7]
print binaryMe(lista, 7, 0, len(lista))
>>>>>>> b2edb34e570bcc63cecabc87d84d6b624edc9900
