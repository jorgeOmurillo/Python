from pythonds.basic.stack import Stack

s = Stack()

s.push('x')
s.push('y')
s.push('z')

while not s.isEmpty():
    s.pop()
    s.pop()
