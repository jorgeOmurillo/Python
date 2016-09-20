class Value:
    def __init__(self, data):
        self.data = data

    def hello(self):
        hello = self.data

newOne = Value(3)

newThree = newOne

newThree.hello = 5

print newOne.hello
