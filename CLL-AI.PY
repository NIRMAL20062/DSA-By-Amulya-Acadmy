class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        if self.head is None:
            print("List is empty")
        if self.head.ref==None:
            print(self.head.data)
        
        else:
            n=self.head
            while True:
                print(n.data, end=" ")
                n=n.ref
                if n==self.head:
                    break
    
    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.ref = self.head 
        else: 
            last_node = self.head
            while last_node.ref != self.head:
                last_node = last_node.ref
            new_node.ref = self.head
            last_node.ref = new_node
            self.head = new_node
    
    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:  # Case: Empty list
            self.head = new_node
            new_node.ref = new_node  # Circular reference to itself
        else:
            last_node = self.head
            while last_node.ref != self.head:
                last_node = last_node.ref
            new_node.ref = self.head
            last_node.ref = new_node




