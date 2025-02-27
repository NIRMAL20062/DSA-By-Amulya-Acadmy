# linear data structure made of chain of nodes each node contains a data field or link or reference.
# linked list is a linear data structure where each element is a separate object.
# Each element, called a node, contains two items: the data and a reference (or link or pointer) to the next node in the sequence. This structure allows for efficient insertion or removal.
# of elements from any position in the sequence.






class node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LL:
    def __init__(self):
        self.head=None
    
    def display(self):
        if self.head==None:
            print('Linked List is empty ')
            return
        n=self.head
        while n:  # The while loop should iterate over n instead of checking n.ref. Otherwise, it will skip the last node.
            print(f'{n.data}-->>',end=' '
                  )
        print('None')

    def insert_begin(self,data):
        if self.head==None:
            print('Linked List is empty so the new node is added as head node')
            self.head = new_node
            return
        new_node=node(data)
        new_node.ref=self.head
        self.head=new_node
    
    def insert_end(self,data):
        new_node=node(data)
        if self.head==None:
            self.head=new_node
            return
        n=self.head
        while n.ref:
            n=n.ref
        n.ref=new_node
    
    def insert_after_node(self,data,x):
        if self.head==None:
            print('Can not append to Empty Node ')
        n=self.head
        while n:
            if n.data==x:
                break
            n=n.ref
        if n!=None:
            




















# 1.Traversal
""" class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, end=" -> ")
                n = n.ref
            print("None")  # Indicates the end of the linked list

# Create a LinkedList instance and test it
ll = LinkedList()
ll.print_LL()      # linked list is empth! """

# Adding Node at the beginning of the linked list.
""" class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class linkedlist:
    def __init__(self):
        self.head=None

    def print_LL(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

lli= linkedlist()
lli.add_begin(10)
lli.add_begin(20)
lli.print_LL() """        # linked list is empth!

""" class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Initialize the next pointer as None

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    def insert_at_beginning(self, data):
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # Point the new node's next to the current head
        self.head = new_node  # Update the head to the new node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
linked_list = LinkedList()
linked_list.insert_at_beginning(10)
linked_list.insert_at_beginning(20)
linked_list.insert_at_beginning(30)
linked_list.display() """

# At the end of the linked list

""" class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class linkedlist:
    def __init__(self):
        self.head=None
    def print_LL(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            n=self.head
            while n is not None:
                print(n.data,'-->',end=' ')
                n=n.ref
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head  # Initialize 'n' to self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

lli= linkedlist()
lli.add_begin(10)
lli.add_end(100)
lli.add_begin(20)
lli.print_LL() """

""" class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Initialize the next pointer as None

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    def insert_at_end(self, data):
        new_node = Node(data)  # Create a new node
        if not self.head:  # If the list is empty, set the new node as the head
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = new_node  # Point the last node's next to the new node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
linked_list = LinkedList()
linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_end(30)
linked_list.display() """


# At between nodes

# here comes two conditions that is it can be added after node and before node

# 1. adding after node
""" class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class linkedlist:
    def __init__(self):
        self.head=None
    def print_LL(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            n=self.head
            while n is not None:
                print(n.data,'-->',end=' ')
                n=n.ref

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.ref
        if n is None:
            print("Node is not present in Linked List")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

lli= linkedlist()
lli.add_begin(10)
lli.add_end(100)
lli.add_after(200,10)
lli.add_begin(20)
lli.print_LL() """

# Add before a node

""" class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class linkedlist:
    def __init__(self):
        self.head=None
    def print_LL(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            n=self.head
            while n is not None:
                print(n.data,'-->',end=' ')
                n=n.ref

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.ref
        if n is None:
            print("Node is not present in Linked List")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    def add_before(self, data, x):
        n = self.head
        if n is None:
            print("Linked List is empty")
        elif n.data == x:
            new_node = Node(data)
            new_node.ref = n
            self.head = new_node
            return
        # here we are traversing the linked list to find the node before the given node
        # if node added on rest of position rather than first position
        else:
            while n.ref is not None:
                if n.ref.data == x:
                    break
                n = n.ref
            if n.ref is None:   #n=self.head
                print("Node is not present in Linked List")
                return
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

lli= linkedlist()
lli.add_begin(10)
lli.add_before(20,10)
lli.add_before(30,299)
lli.print_LL() """

# aading node to a empty linked list

""" class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class linkedlist:
    def __init__(self):
        self.head=None
    def print_LL(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            n=self.head
            while n is not None:
                print(n.data,'-->',end=' ')
                n=n.ref

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.ref
        if n is None:
            print("Node is not present in Linked List")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    def add_before(self, data, x):
        n = self.head
        if n is None:
            print("Linked List is empty")
        elif n.data == x:
            new_node = Node(data)
            new_node.ref = n
            self.head = new_node
            return
        # here we are traversing the linked list to find the node before the given node
        # if node added on rest of position rather than first position
        else:
            while n.ref is not None:
                if n.ref.data == x:
                    break
                n = n.ref
            if n.ref is None:
                print("Node is not present in Linked List")
                return
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not empty")
lli= linkedlist()
lli.insert_empty(12)
lli.print_LL() """

# Removing nodes
# 1.start 2.end 3.middle

""" class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class linkedlist:
    def __init__(self):
        self.head=None
    def print_LL(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            n=self.head
            while n is not None:
                print(n.data,'-->',end=' ')
                n=n.ref

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.ref
        if n is None:
            print("Node is not present in Linked List")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    def add_before(self, data, x):
        n = self.head
        if n is None:
            print("Linked List is empty")
        elif n.data == x:
            new_node = Node(data)
            new_node.ref = n
            self.head = new_node
            return
        # here we are traversing the linked list to find the node before the given node
        # if node added on rest of position rather than first position
        else:
            while n.ref is not None:
                if n.ref.data == x:
                    break
                n = n.ref
            if n.ref is None:
                print("Node is not present in Linked List")
                return
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    def delete_begin(self):
        if self.head is None:
            print("Linked List is 
            empty")
        else:
            self.head = self.head.ref

lli= linkedlist()
lli.add_begin(10)
lli.add_begin(20)
lli.add_begin(30)
lli.delete_begin()
lli.print_LL() """


# delete end node
""" class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class linkedlist:
    def __init__(self):
        self.head=None
    def print_LL(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            n=self.head
            while n is not None:
                print(n.data,'-->',end=' ')
                n=n.ref

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.ref
        if n is None:
            print("Node is not present in Linked List")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    def add_before(self, data, x):
        n = self.head
        if n is None:
            print("Linked List is empty")
        elif n.data == x:
            new_node = Node(data)
            new_node.ref = n
            self.head = new_node
            return
        # here we are traversing the linked list to find the node before the given node
        # if node added on rest of position rather than first position
        else:
            while n.ref is not None:
                if n.ref.data == x:
                    break
                n = n.ref
            if n.ref is None:
                print("Node is not present in Linked List")
                return
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            self.head = self.head.ref

    def delete_end(self):
        if self.head is None:
            print("Linked List is empty")
        elif self.head.ref is None:
            # Only one node in the list
            self.head = None
        else:
            # More than one node in the list
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

            
    def delete_given_node(self, x):
        if self.head is None:
            print('Linked List is empty! Cannot remove element.')
            return
        
        # Case: Head node contains the value to be deleted
        if self.head.data == x:
            self.head = self.head.ref
            print(f'Element {x} deleted successfully.')
            return
        
        n = self.head
        while n.ref:
            if n.ref.data == x:
                n.ref = n.ref.ref  # Skipping the node containing x
                print(f'Element {x} deleted successfully.')
                return
            n = n.ref  # Move to the next node
        
        # If we reach here, the element was not found
        print(f'Element {x} not found in the Linked List.')

    def delete_before_given_node(self,x):
        if self.head==None:
            print('Linked List is empty! Cannot remove element.')
            return
        if self.head.ref.data==x:
            self.head=self.head.ref
            print(f'Element before {x} deleted successfully.')
            return
        n=self.head
        while n.ref:
            if n.ref.ref.data==x:
                n.ref=n.ref.ref
                print(f'Element before {x} deleted successfully.')
                return
            n=n.ref
            print(f'Element before {x} not found in the Linked List.')
    
    def delete_after_given_node(self, x):
        if self.head is None:
            print('Linked List is empty! Cannot remove element.')
            return
        
        n = self.head
        while n and n.ref:
            if n.data == x:
                if n.ref:  # Ensure the next node exists
                    n.ref = n.ref.ref
                    print(f'Element after {x} deleted successfully.')
                    return
                else:
                    print('No node after the given node.')
                    return
            n = n.ref
        
        print(f'Element {x} not found in the Linked List.')
        
    def delete_after_given_node(self, x):
        if self.head is None:
            print('Linked List is empty! Cannot remove element.')
            return

        n = self.head
        # First, check if the next node is None before entering the loop
        while n.ref and n.ref.ref:
            if n.data == x:
                n.ref = n.ref.ref  # Delete the node after the given node
                print(f'Element after {x} deleted successfully.')
                return
            n = n.ref

        print(f'Element {x} not found in the Linked List or no node after {x}.')


lli= linkedlist()
lli.add_begin(12)
lli.add_begin(112)
lli.add_begin(1112)
lli.delete_end()
lli.print_LL() """


