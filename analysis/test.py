from pythonds.basic.stack import Stack

s = Stack()

s.push('x')
s.push('y')
s.push('z')

hola = s.pop()

print hola
print s.peek()

for i in range(10, 200, 30):
    print i
