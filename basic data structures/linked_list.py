class Node:

    def __init__(self, initData):
        self.data = initData
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext


class unorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, data):
        newNode = Node(data)
        newNode.setNext(self.head)
        self.head = newNode

    def size(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False

        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found


def populateList(nums):
    hello = unorderedList()    
    x = 0

    while x < nums: 
        hello.add(x)
        x += 1

    return hello.search(99)

print populateList(11)
