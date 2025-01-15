# Binary tree

class BST:
    # Constructor to initialize the node with a key and set lchild and rchild to None
    def __init__(self, key):
        self.key = key  # Store the value of the node
        self.lchild = None  # Left child of the node
        self.rchild = None  # Right child of the node

    # Method to insert a new data value into the BST
    def insert(self, data):
        # If the tree is empty, initialize the root with the new data
        if self.key is None:
            self.key = data
            return
        
        # If the data already exists in the tree, do nothing (avoid duplicates)
        if self.key == data:
            return

        # If the new data is less than the current node's key, insert it into the left subtree
        if self.key > data:
            if self.lchild:  # If a left child exists, insert recursively
                self.lchild.insert(data)
            else:  # If no left child, create a new node for the left child
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
root.postorder()