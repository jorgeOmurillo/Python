class Stack():
    def __init__(self):
        self.lista = []

    def append(self, value):
        self.lista.append(value)

    def delete(self):
        return self.lista.pop()

    def size(self):
        return len(self.lista)


hello = Stack()
hello.append(1)
hello.append(2)
hello.append(3)
hello.append(4)
hello.append(5)

# print(hello.size())
# print(hello.delete())
# print(hello.size())

while hello.size() > 0:
    print(hello.delete())
