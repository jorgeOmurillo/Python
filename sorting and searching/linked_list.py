class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_node(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next_node = self.head
            self.head = new_node
        self.size += 1

    def get_size(self):
        return self.size

    def print_list(self):

        current = self.head

        while current:
            print(current.data)
            current = current.next_node

    def search(self, value):
        current = self.head
        found = False

        while not found and current:
            if current.data == value:
                found = True
                return found
            else:
                current = current.next_node

        return found

    def delete_node(self, value):
        current = self.head
        found = False
        previous = None

        while not found and current:
            if current.data == value:
                found = True
            else:
                previous = current
                current = current.next_node

        if current == None:
            print("Node does not exist.")
            return False
        if previous == None:
            self.head = current.next_node
            self.size -= 1
        else:
            previous.next_node = current.next_node
            self.size -= 1

hello = LinkedList()
hello.insert_node(4)
hello.insert_node(1)
hello.insert_node(2)
hello.insert_node(5)
hello.insert_node(1123)
hello.insert_node(199)

# hello.print_list()

# print(hello.search(2))
# print(hello.search(123))

hello.delete_node(199)
hello.delete_node(111)

hello.print_list()
print("List size is: ", hello.get_size())
