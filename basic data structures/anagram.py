import time

def anagram(s1, s2):

    lista = list(s2)

    pos1 = 0
    OK = True

    while pos1 < len(s1) and OK:
        pos2 = 0
        found = False

        while pos2 < len(lista) and not found:
            if s1[pos1] == lista[pos2]:
                found = True
            else:
                pos2 += 1

        if found:
            lista[pos2] = None
        else:
            OK = False

        pos1 += 1

    return OK

def anagram2(s1, s2):
    lista1 = list(s1)
    lista2 = list(s2)

    lista1.sort()
    lista2.sort()

    pos = 0
    match = True

    while pos < len(s1) and match:
        if lista1[pos] == lista2[pos]:
            pos += 1
        else:
            match = False

    return match

def anagram4(s1, s2):
    counter1 = [0]*26
    counter2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        counter1[pos] += 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        counter2[pos] += 1

    j = 0
    OK = True

    while j < 26 and OK:
        if counter1[j] == counter2[j]:
            j += 1
        else:
            OK = False

    return OK

print anagram('abcd', 'dcba')
print anagram2('abcd', 'dcba')
print anagram4('abcd', 'dcba')
