class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.left = None
        self.right = None

    def insert_left(self, value):
        if self.left == None:
            self.left = BinaryTree(value)
        else:
            temp = BinaryTree(value)
            temp.left = self.left
            self.left = temp

    def insert_right(self, value):
        if self.right == None:
            self.right = BinaryTree(value)
        else:
            temp = BinaryTree(value)
            temp.right = self.right
            self.righ = temp

    def get_right_child(self):
        return self.right

    def get_left_child(self):
        return self.left

    def set_root(self, value):
        self.key = value

    def get_root(self):
        return self.key

r = BinaryTree('a')
print(r.get_root())
print(r.get_left_child())
r.insert_left('b')
print(r.get_left_child())
print(r.get_left_child().get_root())
r.insert_right('c')
print(r.get_right_child())
print(r.get_right_child().get_root())
r.get_right_child().set_root('hello')
print(r.get_right_child().get_root())
