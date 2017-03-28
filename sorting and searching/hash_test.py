def hashThis(lista,num):

    hashed = [None]*num
    res = 0
    
    for i in range(len(list)):
       res = i%num 
       print res
       hashed[i] = i%num
    
    print hashed

listMe = [10,33,4]

hashThis(listMe, 5)
