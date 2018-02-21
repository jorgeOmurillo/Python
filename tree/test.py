# import queue

# class BinarySearchTree():

    # def __init__(self, value):
        # self.value = value
        # self.left_node = None
        # self.right_node = None

    # def insert_node(self, value):
        # if value <= self.value and self.left_node:
            # self.left_node.insert_node(value)
        # elif value <= self.value:
            # self.left_node = BinarySearchTree(value)
        # elif value > self.value and self.right_node:
            # self.right_node.insert_node(value)
        # else:
            # self.right_node = BinarySearchTree(value)

    # def bst(self):
        # q = queue.Queue()
        # q.put(self)

        # while not q.empty():
            # current_node = q.get()
            # print(current_node.value)

            # if current_node.left_node:
                # q.put(current_node.left_node)
            # if current_node.right_node:
                # q.put(current_node.right_node)

    # def search(self, value):
        # if value < self.value and self.left_node:
            # return self.left_node.search(value)
        # if value > self.value and self.right_node:
            # return self.right_node.search(value)
        
        # print(self.value == value)


# hello = BinarySearchTree(5)

# hello.insert_node(1)
# hello.insert_node(44)
# hello.insert_node(555)
# hello.insert_node(7)
# hello.insert_node(1)
# hello.insert_node(5)
# hello.insert_node(9)
# hello.insert_node(100)
# hello.insert_node(71)
# hello.insert_node(41)
# hello.insert_node(29)
# hello.insert_node(233)


# # hello.bst()
# hello.search(1)

# 128 64 32 16 8 4 2 1 == 255
num = 6<<2
text = 5>>1

print(num, text)
