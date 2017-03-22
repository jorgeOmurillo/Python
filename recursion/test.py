textThis = open('sample.txt', 'r')
f = textThis.read()

bet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
dick = {}

for i in f:
    if i in bet:
        dick[i] += 1

print dick
