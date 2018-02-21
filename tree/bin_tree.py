import queue

class BinaryT():

    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None

    def insert_left_node(self, value):
        if self.left_node == None:
            self.left_node = BinaryT(value)
        else:
            newN = BinaryT(value)
            newN.left_node = self.left_node
            self.left_node = newN

    def insert_right_node(self, value):
        if self.right_node == None:
            self.right_node = BinaryT(value)
        else:
            newN = BinaryT(value)
            newN.right_node = self.right_node
            self.right_node = newN

    def pre_order(self):
        print(self.value)

        if self.left_node:
            self.left_node.pre_order()
        if self.right_node:
            self.right_node.pre_order()

    def in_order(self):
        if self.left_node:
            self.left_node.pre_order()
        
        print(self.value)

        if self.right_node:
            self.right_node.pre_order()

    def post_order(self):
        if self.left_node:
            self.left_node.pre_order()
        if self.right_node:
            self.left_node.pre_order()

        print(self.value)

    def bfs(self):
        q = queue.Queue()
        q.put(self)

        while not q.empty():
            current_node = q.get()
            print(current_node.value)

            if current_node.left_node:
                q.put(current_node.left_node)
            if current_node.right_node:
                q.put(current_node.right_node)

    def dfs(self):
        lista = []
        lista.append(self.value)

        if self.left_node:
            self.left_node.dfs()
        if self.right_node:
            self.right_node.dfs()

        return lista


a = BinaryT('a')
a.insert_left_node('b')
a.insert_right_node('c')

b = a.left_node
c = a.right_node

c.insert_left_node('d')
c.insert_right_node('e')

d = c.left_node
e = c.right_node

# a.pre_order()
# a.in_order()
# a.post_order()
# a.bfs()
print(a.dfs())
