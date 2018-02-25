class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class OrderedLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_node(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            current = self.head
            previous = None
            found = False

            while not found and current is not None:
                if current.data < new_node.data:
                    found = True
                else:
                    previous = current
                    current = current.next

            if previous == None:
                new_node.next = self.head
                self.head = new_node
            else:
                new_node.next = current
                previous.next = new_node
 
    def print_list(self):
        current = self.head

        while current:
            print(current.data)
            current = current.next

lista = OrderedLinkedList()

lista.insert_node(7)
lista.insert_node(2)
lista.insert_node(5)
lista.insert_node(3)
lista.insert_node(1)
lista.insert_node(4)

lista.print_list()
