import math

wordlist = ['conejo', 'perro', 'raton', 'gato']
letterlist = []

count =0
contar = 0

for aword in wordlist:
    count += 1
    for aletter in aword:
        contar +=1
        letterlist.append(aletter)
print letterlist
print count
print contar

n = 2

if n<0:
    print "Sorry"
else:
    print math.sqrt(n)

sqlist = []

for x in range(1,11):
    sqlist.append(x*x)

print sqlist

newlist = [x*3 for x in range(1,11)]

print newlist
