def hashThis(lista):

    hashed = [None]*len(lista)
    res = 0
 
    for i in lista:
       res = i%len(lista) 
 
       if hashed[res] is None:
           hashed[res] = i
       else:
           count = res
 
           while hashed[count] is not None:
               if count < len(hashed) - 1:
                   count += 1
               else:
                   count = 0

           hashed[count] = i
    print hashed
    
    return hashed

def position(lista, num):
    
    found = False
    count = 0

    while not found and count < len(lista)-1:
        if num == lista[count]:
            found = True
        else:
            count += 1
    return found


listMe = [113 , 117 , 97 , 100 , 114 , 108 , 116 , 105 , 99]

print position(hashThis(listMe), 22)
