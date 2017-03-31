class MyTest:

    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def addMe(self, item, data):

        myvalue = self.defineMe(item, len(self.slots))

        self.slots[myvalue] = item
        self.data[myvalue] = data

    def defineMe(self, item, size):
        return item % size

    def __setitem__(self, item, data):
        self.addMe(item,data)


j = MyTest()
j[1] = "hi"

print "type:",type(j.slots),j.slots
print "type:",type(j.data),j.data
