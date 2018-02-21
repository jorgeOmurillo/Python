class Queue():
    def __init__(self):
        self.queue = []

    def add(self, value):
        self.queue.insert(0, value)

    def get(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)

hello = Queue()
hello.add(1)
hello.add(2)
hello.add(3)
hello.add(4)
hello.add(5)

while hello.size() > 0:
    print(hello.get())
