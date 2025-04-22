""" # Binary tree

class BST:
    # Constructor to initialize the node with a key and set lchild and rchild to None
    def __init__(self, key):
        self.key = key  # Store the value of the node
        self.lchild = None  # Left child of the node
        self.rchild = None  # Right child of the node

    # Method to insert a new data value into the BST
    def insert(self, data):
    
        # no need babyyyy If the tree is empty, initialize the root with the new data
        # if self.key is None:
        #     self.key = data
        #     return
        
        # If the data already exists in the tree, do nothing (avoid duplicates)
        if self.key == data:
            return 

        # If the new data is less than the current node's key, insert it into the left subtree
        if self.key > data:
            if self.lchild:  # If a left child exists, insert recursively
                self.lchild.insert(data)
            else:  # If no left child, create a new node for the left child and insert data 
                self.lchild = BST(data)
        # If the new data is greater than the current node's key, insert it into the right subtree
        else:
            if self.rchild:  # If a right child exists, insert recursively
                self.rchild.insert(data)
            else:  # If no right child, create a new node for the right child
                self.rchild = BST(data)


    def search(self, data):
        # Check if the current node's key matches the data being searched
        if self.key == data:
            print('Node is found')  # Node found
            return

        # If the data to be searched is less than the current node's key, search in the left subtree
        if data < self.key:
            if self.lchild:  # If a left child exists, recursively search in the left subtree
                self.lchild.search(data)
            else:
                print('Node is not present in tree')  # Left child is None, node not found

        # If the data to be searched is greater than the current node's key, search in the right subtree
        else:
            if self.rchild:  # If a right child exists, recursively search in the right subtree
                self.rchild.search(data)
            else:
                print('Node is not present in tree')  # Right child is None, node not found


# traversal
    def preorder(self):
        print(self.key, end=' ')
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key, end=' ')
        if self.rchild:
            self.rchild.inorder()

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key, end=' ')

    def delete(self,data):
        if self.key is None:
            print('tree is empty! ')
            return
        if data <self.key:
            if self.lchild:
                self.lchild=self.lchild.delete(data)
            else:
                print('Given node is not present in the tree! ')
        elif data>self.key:
            if self.rchild:
                self.rchild=self.rchild.delete(data)
            else:
                print('Given Node is not present in the tree ! ')
        # else:

root = BST(10)
list1 = [20, 4, 5, 15, 2, 8, 12, 18]
for i in list1:
    root.insert(i)
root.search(155)
print('Preorder Traversal:')
root.preorder()
print('inorder Traversal:')
root.inorder()
print('Postorder Traversal:')
root.postorder() """


""" class BTS:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    
    def insert(self,data):
        if self.key==data:
            return
        if self.key>data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BTS(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BTS(data)
    
    def search(self,data):
        if self.key==data:
            return True
        if self.key>data:
            if self.lchild:
                return self.lchild.search(data)
            else:
                return False
        else:
            if self.rchild:
                return self.rchild.search(data)
            else:
                return False
    
    def preOrder(self):
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.preOrder()
        if self.rchild:  # Note :if hi use krna hai , elif kroge tab dekho agr chile ka right node rha toh uska serch nhi ho payega na isliye hame sabko check krna hai 
            self.rchild.preOrder()

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key, end=' ')
        if self.rchild:
            self.rchild.inorder()

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key, end=' ')

    
    # deletion operation

    def delete(self,data):
        if self.key is None:
            print('Tree is Empty')
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                print('Given node is not present in the Tree')
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print('Given Node is Not Present in the Tree')
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            node =self.rchild
            while node.lchild:
                node= node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key)
        return self


root = BTS(10)
list1 = [20, 4, 5, 15, 2, 8 , 12, 18]
for i in list1:
    root.insert(i)

root.delete(8)  # Deleting a leaf node (8)
print(root.inorder())  # Expected: 2 4 5 10 12 15 18 20 (without 8)

root.delete(15)  # Node 15 has a right child (18)
print(root.inorder())  # Expected: 2 4 5 10 12 18 20 (without 15)

root.delete(4)  # Node 4 has two children (2, 5)
print(root.inorder())  # Expected: 2 5 10 12 15 18 20 (without 4) """




# Final CODE
class BST:
    def __init__(self, key):
        #Initialize a node with a given key, setting left and right children to None.
        self.key = key
        self.lchild = None  # Left child (smaller values)
        self.rchild = None  # Right child (greater values)
    
    def insert(self, data):
        # Insert a new node into the BST following the BST property.
        if self.key == data:
            return  # Ignore duplicates
        if data < self.key:
            # Insert in the left subtree
            self.lchild = self.lchild.insert(data) if self.lchild else BST(data)
        else:
            # Insert in the right subtree
            self.rchild = self.rchild.insert(data) if self.rchild else BST(data)
        
        return self  # Return the current node

    def search(self, data):
        # Search for a value in the BST.
        if self.key == data:
            return True  # Found the value
        
        if data < self.key and self.lchild:
            return self.lchild.search(data)  # Search in the left subtree
        
        if data > self.key and self.rchild:
            return self.rchild.search(data)  # Search in the right subtree
        
        return False  # Not found
    
    def preorder(self):
        # Print preorder traversal (Root -> Left -> Right).
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    
    def inorder(self):
        # Print inorder traversal (Left -> Root -> Right).
        if self.lchild:
            self.lchild.inorder()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.inorder()
    
    def postorder(self):
        # Print postorder traversal (Left -> Right -> Root).
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key, end=" ")
    
    def delete(self, data):
        # Delete a node from the BST while maintaining BST properties.
        if data < self.key:
            # If data is smaller, look in the left subtree
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                print(f"{data} not found in tree")
        elif data > self.key:
            # If data is larger, look in the right subtree
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print(f"{data} not found in tree")
        else:
            # Found the node to be deleted
            
            # Case 1: Node has no children
            if self.lchild is None and self.rchild is None:
                return None  # Remove leaf node

            # Case 2: Node has only one child
            if self.lchild is None:
                return self.rchild  # Replace with right child
            elif self.rchild is None:
                return self.lchild  # Replace with left child

            # Case 3: Node has two children
            temp = self.rchild  # Find the inorder successor (smallest in right subtree)
            while temp.lchild:
                temp = temp.lchild
            
            self.key = temp.key  # Copy inorder successor value
            self.rchild = self.rchild.delete(temp.key)  # Delete inorder successor

        return self  # Return updated node

    def min_node(self):
        # Find the node with the smallest key in the BST.
        current = self
        while current.lchild:
            current = current.lchild
        return current.key

    def max_node(self):
        # Find the node with the largest key in the BST.
        current = self
        while current.rchild:
            current = current.rchild
        return current.key

    def __str__(self):
        # Return a string representation of the BST node.
        return f"BST(key={self.key}, left={self.lchild.key if self.lchild else None}, right={self.rchild.key if self.rchild else None})"


# Example usage
if __name__ == "__main__":
    root = BST(50)  # Create the root node
    nums = [30, 70, 20, 40, 60, 80]  # List of numbers to insert into BST
    
    for num in nums:
        root.insert(num)  # Insert each number into BST
    
    print("\nInorder traversal (Sorted Order):")
    root.inorder()  # Output: 20 30 40 50 60 70 80
    
    print("\n\nPreorder traversal:")
    root.preorder()  # Output: 50 30 20 40 70 60 80
    
    print("\n\nPostorder traversal:")
    root.postorder()  # Output: 20 40 30 60 80 70 50
    
    print("\n\nSearch 40:", root.search(40))  # True (40 is in BST)
    print("Search 99:", root.search(99))  # False (99 is not in BST)
    
    print("\nDeleting 50:")
    root = root.delete(50)  # Delete the root node (50)
    
    print("New Inorder traversal after deletion:")
    root.inorder()  # Output: 20 30 40 60 70 80
    print()

    print('Min Node:', root.min_node())  # Output: 20
    print('Max Node:', root.max_node())  # Output: 80
array =[1,2,3,4,5,6]
key=4
def binary(array):
    key=4
    left=0
    right=len(array)-1
    while left<=right:
        mid=(left+right)//2
        if array[mid]==key:
            return mid
        elif array[mid]<key:
            left=mid+1
        else:
            right=mid-1
    return -1
print(binary(array)) 
