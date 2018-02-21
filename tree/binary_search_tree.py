class BinarySearchTree():

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_node(self, value):
        if value <= self.value and self.left_child:
            self.left_child.insert_node(value)
        elif value <= self.value:
            self.left_child = BinarySearchTree(value)
        elif value > self.value and self.right_child:
            self.right_child.insert_node(value)
        else:
            self.right_child = BinarySearchTree(value)

    def search(self, value):
        if value < self.value and self.left_child:
            return self.left_child.search(value)
        if value > self.value and self.right_child:
            return self.right_child.search(value)

        print(value == self.value)

    def pre_order(self):
        print(self.value)

        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()

    def remove(self, value, parent):
        if value < self.value and self.left_child:
            return self.left_child.remove(value, self)
        elif value < self.value:
            return False
        elif value > self.value and self.right_child:
            return self.right_child.remove(value, self)
        elif value > self.value:
            return False
        else:
            if self.left_child is None and self.right_child is None and self == parent.left_child:
                parent.left_child = None
                self.clear_node()
            elif self.left_child is None and self.right_child is None and self == parent.right_child:
                parent.right_child = None
                self.clear_node()
            elif self.left_child and self.right_child is None and self == parent.left_child:
                parent.left_child = self.left_child
                self.clear_node()
            elif self.left_child and self.right_child is None and self == parent.right_child:
                parent.right_child = self.left_child
                self.clear_node()
            elif self.right_child and self.left_child is None and self == parent.left_child:
                parent.left_child = self.right_child
                self.clear_node()
            elif self.right_child and self.left_child is None and self == parent.right_child:
                parent.right_child = self.right_child
                self.clear_node()
            else:
                self.value = self.right_child.find_minimum()
                self.right_child.remove(self.value, self)
            return True

    def clear_node(self):
        self.value = None
        self.left_child = None
        self.right_child = None

    def find_minimum(self):
        if self.left_child:
            return self.left_child.find_minimum()
        else:
            return self.value


test = BinarySearchTree(5)
test.insert_node(10)
test.insert_node(8)
test.insert_node(12)
test.insert_node(20)
test.insert_node(17)
test.insert_node(25)
test.insert_node(19)

test.pre_order()
test.search(1123)
