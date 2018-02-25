class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None
        self.previous_node = None

    def get_next_node(self):
        return self.next_node

    def get_previous_node(self):
        return self.previous_node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get_size(self):
        return self.size

    def insert_node(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next_node = self.head
            self.head.previous_node = new_node
            self.head = new_node
        self.size += 1

    def remove(self, data):
        current = self.head
        found = False
        
        while not found and current:
            if current.data == data:
                found = True
                if current == None:
                    print("Node does not exist.")
                    return found
                elif current.previous_node == None:
                    self.head = current.next_node
                    self.size -= 1
                    print("Node removed.")
                elif current.next_node == None:
                    current.previous_node.next_node = None
                    self.size -= 1
                    print("Node removed.")
                else:
                    current.previous_node.next_node = current.next_node
                    current.next_node.previous_node = current.previous_node
                    self.size -= 1
                    print("Node removed.")
            else:
                current = current.next_node

    def print_list(self):
        if self.head == None:
            print("List is empty.")
        else:
            current = self.head

            while current:
                print(current.data)
                current = current.get_next_node()

hello = DoublyLinkedList()
hello.insert_node(1)
hello.insert_node(2)
hello.insert_node(3)
hello.insert_node(5)

hello.remove(5)

hello.print_list()
print("Size is ", hello.size)
