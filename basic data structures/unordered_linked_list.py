import random

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

        if self.isEmpty:
            raise Exception("There are no nodes to remove!")

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
        current = self.head

        while current != None:
            print current.getData()
            current = current.getNext()

    def appendNode(self, item):
        current = self.head
        previous = None
        newNode = Node(item)

        while current != None:
            previous = current
            current = current.getNext()

        previous.setNext(newNode)

    def insertNode(self, pos, item):
        current = self.head
        previous = None
        position = 0
        newNode = Node(item)
        found = False

        while not found:
            if position == pos:
                found = True
            else:
                previous = current
                current = current.getNext()
                position += 1
        
        if previous == None:
            newNode.setNext(self.head)            
            self.head = newNode
        else:
            newNode.setNext(previous.getNext())
            previous.setNext(newNode)

    def popNode(self, index):
        current = self.head
        position = 0
        found = False
        previous = None

        if self.isEmpty:
            raise Exception("There are no nodes to remove!")        

        if index == None:
            index = self.size-1

        while not found:
            if position == index:
                found = True
            else:
                position += 1
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
            print "popped ", current.getData()
        else:
            previous.setNext(current.getNext())
            print "popped ", current.getData()


def populateList(nums):
    hello = unorderedList()    
    x = 1

    while x <= nums: 
        #hello.add(random.randrange(100, 200))
        hello.add(x)
        x += 1

    #hello.insertNode(9, "lo logre!")
    hello.popNode(1)
    hello.popNode(2)


    hello.printList()

populateList(1)
