def hashThis(lista,num):

    hashed = {}
    res = 0
    
    for i in lista:
       res = i%num 
       print res
       hashed[i] = i%num
    
    print hashed

listMe = [10,33,4]

hashThis(listMe, 3)
