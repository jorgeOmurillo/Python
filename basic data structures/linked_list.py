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

    def searchNode(self, item):
        current = self.head
        found = False

        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def removeNode(self, item):
        current = self.head
        found = False
        previous = None

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def printList(self):
        found = False
        current = self.head

        while current != None and not found:
            print current.getData()
            current = current.getNext()


def populateList(nums):
    hello = unorderedList()    
    x = 1

    while x < nums: 
        hello.add(x)
        x += 1

    hello.removeNode(11)

    hello.printList()

populateList(11)
