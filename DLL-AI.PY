# Node class to represent each node in the doubly linked list
class Node:
    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.nref = None  # Reference to the next node
        self.pref = None  # Reference to the previous node


# Doubly_LL class to represent the doubly linked list
class Doubly_LL:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None 
 
    # Method to display the doubly linked list 
    def Display(self):
        if self.head is None:  # If the list is empty
            print('Doubly Linked List Is Empty')
            return
        n = self.head
        while n is not None:  # Traverse the list
            print(f'{n.data} -->> ', end=' ')  # Print the current node's data
            n = n.nref  # Move to the next node
        print('None')  # Indicate the end of the list

    # Method to display the doubly linked list in reverse order
    def reverse_Doubly_LL(self):
        if self.head is None:  # If the list is empty
            print('Doubly Linked List is Empty ')
            return
        n = self.head
        while n.nref is not None:  # Traverse to the last node
            n = n.nref
        while n is not None:  # Traverse backward using `pref`
            print(f'{n.data} -->>', end=' ')
            n = n.pref
        print()  # Print a newline after the list

    # Method to insert a node at the beginning of the list
    def Insert_begin(self, data):
        new_node = Node(data)  # Create a new node
        if self.head is None:  # If the list is empty
            self.head = new_node  # Set the new node as the head
        else:
            new_node.nref = self.head  # New node's next points to the current head
            self.head.pref = new_node  # Current head's previous points to the new node
            self.head = new_node  # Update the head to the new node
        self.Display()  # Display the updated list

    # Method to insert a node at the end of the list
    def insert_last(self, data):
        new_node = Node(data)  # Create a new node
        if self.head is None:  # If the list is empty
            self.head = new_node  # Set the new node as the head
        else:
            n = self.head
            while n.nref is not None:  # Traverse to the last node
                n = n.nref
            n.nref = new_node  # Last node's next points to the new node
            new_node.pref = n  # New node's previous points to the last node
        self.Display()  # Display the updated list

    # Method to insert a node after a given node with value `x`
    def insert_after_node(self, data, x):
        if self.head is None:  # If the list is empty
            print("Doubly Linked List is empty.")
            return
        n = self.head
        while n is not None:  # Traverse the list to find the node with value `x`
            if n.data == x:  # If the node is found
                new_node = Node(data)  # Create a new node
                new_node.nref = n.nref  # New node's next points to the next node of `n`
                new_node.pref = n  # New node's previous points to `n`
                if n.nref is not None:  # If `n` is not the last node
                    n.nref.pref = new_node  # Update the next node's previous to the new node
                n.nref = new_node  # `n`'s next points to the new node
                self.Display()  # Display the updated list
                return
            n = n.nref  # Move to the next node
        print(f"Node with data {x} not found in the Linked List.")  # If `x` is not found 

    # Method to insert a node before a given node with value `x`
    def insert_before(self, data, x):
        if self.head is None:  # If the list is empty
            print("Doubly Linked List is empty.")
            return
        if self.head.data == x:  # If `x` is the head node
            new_node = Node(data)  # Create a new node
            new_node.nref = self.head  # New node's next points to the current head
            self.head.pref = new_node  # Current head's previous points to the new node
            self.head = new_node  # Update the head to the new node
            return
        n = self.head
        while n is not None:  # Traverse the list to find the node with value `x`
            if n.nref is not None and n.nref.data == x:  # If the next node has value `x`
                new_node = Node(data)  # Create a new node
                new_node.nref = n.nref  # New node's next points to the node with value `x`
                new_node.pref = n  # New node's previous points to `n`
                n.nref.pref = new_node  # Update the next node's previous to the new node
                n.nref = new_node  # `n`'s next points to the new node
                return
            n = n.nref  # Move to the next node
        print(f"Node with data {x} not found in the Linked List.")  # If `x` is not found

    # Method to delete the first node of the list
    def delete_first(self):
        if self.head is None:  # If the list is empty
            print("Doubly Linked List is empty.")
            return
        if self.head.nref is None:  # If the list has only one node
            self.head = None  # Remove the head node
        else:
            self.head = self.head.nref  # Update the head to the next node
            self.head.pref = None  # Set the new head's previous to None
        self.Display()  # Display the updated list

    # Method to delete the last node of the list
    def delete_end(self):
        if self.head is None:  # If the list is empty
            print("Doubly Linked List is empty.")
            return
        if self.head.nref is None:  # If the list has only one node
            self.head = None  # Remove the head node
        else:
            n = self.head
            while n.nref.nref is not None:  # Traverse to the second-to-last node
                n = n.nref
            n.nref = None  # Remove the last node
        self.Display()  # Display the updated list

    # Method to delete a node with a given value `x`
    def delete_given_node(self, x):
        if self.head is None:  # If the list is empty
            print("Linked list is empty.")
            return
        if self.head.data == x:  # If the node to delete is the head node
            self.head = self.head.nref  # Update the head to the next node
            if self.head:  # If the new head exists
                self.head.pref = None  # Set the new head's previous to None
            return
        n = self.head 
        while n and n.nref:  # Traverse the list to find the node with value `x`
            if n.nref.data == x:  # If the next node has value `x`
                n.nref = n.nref.nref  # Skip the node with value `x`
                if n.nref:  # If there is a node after the deleted node
                    n.nref.pref = n  # Update the next node's previous to `n`
                return
            n = n.nref  # Move to the next node 
        print(f"Node with value {x} not found in the linked list.")  # If `x` is not found

    # Method to delete the node after a given node with value `x`
    def delete_after(self, x):
        if self.head is None:  # If the list is empty
            print("Linked list is empty.")
            return
        n = self.head
        while n and n.nref:  # Traverse the list to find the node with value `x`
            if n.data == x:  # If the node is found
                n.nref = n.nref.nref  # Skip the next node
                if n.nref:  # If there is a node after the deleted node
                    n.nref.pref = n  # Update the next node's previous to `n`
                return
            n = n.nref  # Move to the next node
        print(f"Node with value {x} not found or no node after it to delete.")  # If `x` is not found

    # Method to delete the node before a given node with value `x`
    def delete_before(self, x):
        if self.head is None:  # If the list is empty
            print("Linked list is empty.")
            return
        if self.head.data == x:  # If `x` is the head node
            print("No node before the head node to delete.")
            return
        n = self.head 
        while n and n.nref:  # Traverse the list to find the node with value `x`
            if n.nref.data == x:  # If the next node has value `x`
                n.nref = n.nref.nref  # Skip the node before `x`
                if n.nref:  # If there is a node after the deleted node
                    n.nref.pref = n  # Update the next node's previous to `n`
                return
            n = n.nref  # Move to the next node
        print(f"Node with value {x} not found or no node before it to delete.")  # If `x` is not found



dll = Doubly_LL()
dll.Insert_begin(10)
dll.insert_last(20)
dll.insert_after_node(15, 10)
dll.insert_before(5, 10)
dll.delete_first()
dll.delete_end()
dll.delete_given_node(15)
dll.delete_after(10)
dll.delete_before(20)
dll.reverse_Doubly_LL()