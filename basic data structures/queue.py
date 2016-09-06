class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

newQueue = Queue()

newQueue.enqueue(1)
newQueue.enqueue("Jorge")
print newQueue.size()

newQueue.dequeue()

print newQueue.size()
