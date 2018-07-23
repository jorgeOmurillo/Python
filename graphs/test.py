wfile = open("hello.txt", 'r')
hello = wfile.read()

for word in hello.split():
    print(word, len(word))

def hi(n):
    yield from range(n, 0, -1)
    yield from range(n)

print(list(hi(5)))

for x in range(-1, 0, -1):
    print(x)
