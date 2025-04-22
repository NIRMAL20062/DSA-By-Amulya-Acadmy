# Node class to represent each node in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.ref = None   # Reference to the next node 


# Linkedlist class to represent the linked list
class Linkedlist:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    def length(self):
        count = 0 
        n = self.head
        while n:
            count += 1
            n = n.ref
        return count

    # Method to display the linked list
    def display(self):
        if self.head is None:  # If the list is empty
            print("Linked List Is Empty !!! 👽")
            return
        n = self.head
        while n is not None:  # Traverse the list
            print(f'| {n.data} | --->', end=' ')  # Print the current node's data
            n = n.ref  # Move to the next node
        print("None")  # Indicate the end of the list

    # Method to insert a node at the beginning of the list
    def insert_initial(self, data):
        new_node = Node(data)  # Create a new node
        if self.head is None:  # If the list is empty
            self.head = new_node  # Set the new node as the head
        else:
            new_node.ref = self.head  # New node's next points to the current head
            self.head = new_node  # Update the head to the new node 

    # Method to insert a node at the end of the list
    def insert_end(self, data):
        new_node = Node(data)  # Create a new node
        if self.head is None:  # If the list is empty
            self.head = new_node  # Set the new node as the head
        else:
            n = self.head
            while n.ref is not None:  # Traverse to the last node
                n = n.ref
            n.ref = new_node  # Last node's next points to the new node

    # Method to insert a node before a given node with value `x`
    def insert_before(self, data, x):
        new_node = Node(data)  # Create a new node
        if self.head is None:  # If the list is empty
            print("Linked List is empty. Cannot insert before non-existent node.")
            return
        if self.head.data == x:  # If `x` is the head node
            new_node.ref = self.head  # New node's next points to the current head
            self.head = new_node  # Update the head to the new node
            return
        n = self.head
        while n.ref is not None:  # Traverse the list to find the node before `x`
            if n.ref.data == x:  # If the next node has value `x`
                new_node.ref = n.ref  # New node's next points to the node with value `x`
                n.ref = new_node  # Current node's next points to the new node
                return
            n = n.ref  # Move to the next node
        print(f"Node with data {x} not found in the Linked List.")  # If `x` is not found

    # Method to insert a node after a given node with value `x`
    def insert_after(self, data, x):
        new_node = Node(data)  # Create a new node
        if self.head is None:  # If the list is empty
            print("Linked List is empty.")
            return
        n = self.head
        while n is not None:  # Traverse the list to find the node with value `x`
            if n.data == x:  # If the node is found
                new_node.ref = n.ref  # New node's next points to the next node of `n`
                n.ref = new_node  # `n`'s next points to the new node
                return
            n = n.ref  # Move to the next node
        print(f"Node with data {x} not found in the Linked List.")  # If `x` is not found

    # Method to delete the first node of the list
    def delete_begin(self):
        if self.head is None:  # If the list is empty
            print('Linked List is empty! Cannot remove element.')
            return
        self.head = self.head.ref  # Move the head to the next node

    # Method to delete the last node of the list
    def delete_end(self):
        if self.head is None:  # If the list is empty
            print('Linked List is empty! Cannot remove element.')
            return
        if self.head.ref is None:  # If the list has only one node
            self.head = None  # Remove the head node
        else:
            n = self.head
            while n.ref.ref is not None:  # Traverse to the second-to-last node
                n = n.ref 
            n.ref = None  # Remove the last node

    # Method to delete a node with a given value `x`
    def delete_given_node(self, x):
        if self.head is None:  # If the list is empty
            print('Linked List is empty! Cannot remove element.')
            return
        if self.head.data == x:  # If the node to delete is the head node
            self.head = self.head.ref  # Update the head to the next node
            print(f'Element {x} deleted successfully.')
            return
        n = self.head
        while n.ref is not None:  # Traverse the list to find the node with value `x`
            if n.ref.data == x:  # If the next node has value `x`
                n.ref = n.ref.ref  # Skip the node with value `x`
                print(f'Element {x} deleted successfully.')
                return
            n = n.ref  # Move to the next node
        print(f'Element {x} not found in the Linked List.')  # If `x` is not found 

    # Method to delete the node before a given node with value `x`
    def delete_before_given_node(self, x):
        if self.head is None or self.head.ref is None:  # If the list is empty or has only one node
            print("Linked List is empty or does not have enough elements to delete.")
            return
        if self.head.data == x:  # If `x` is the head node
            print(f"No node exists before {x} to delete.")
            return
        if self.head.ref.data == x:  # If the second node is `x`
            self.head = self.head.ref  # Delete the head node
            print(f"Element before {x} deleted successfully.")
            return 
        n = self.head
        while n.ref.ref is not None:  # Traverse the list to find the node before `x`
            if n.ref.ref.data == x:  # If the node after the next node has value `x`
                n.ref = n.ref.ref  # Skip the node before `x`
                print(f"Element before {x} deleted successfully.")
                return 
            n = n.ref  # Move to the next node
        print(f"Element before {x} not found in the Linked List.")  # If `x` is not found

    # Method to delete the node after a given node with value `x`
    def delete_after(self, x):
        if self.head is None:  # If the list is empty
            print("Linked List is empty.")
            return
        n = self.head
        while n is not None:  # Traverse the list to find the node with value `x`
            if n.data == x:  # If the node is found
                if n.ref is None:  # If `x` is the last node
                    print(f"No node exists after {x} to delete.")
                    return
                n.ref = n.ref.ref  # Skip the node after `x`
                print(f"Element after {x} deleted successfully.")
                return
            n = n.ref  # Move to the next node
        print(f"Element {x} not found in the Linked List.")  # If `x` is not found 


# Create a linked list
ll = Linkedlist()

# Insert elements
ll.insert_initial(10)
ll.insert_end(20)
ll.insert_after(15, 10)
ll.insert_before(5, 10)

# Display the list
ll.display()  # Output: | 5 | ---> | 10 | ---> | 15 | ---> | 20 | ---> None

# Delete elements
ll.delete_begin()
ll.delete_end()
ll.delete_given_node(15)
ll.delete_after(10)
ll.delete_before_given_node(20)

# Display the updated list
ll.display()  # Output: | 10 | ---> None