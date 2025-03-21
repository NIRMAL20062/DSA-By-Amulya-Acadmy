# doubly linked list
# while n is not None:	Last node	Printing all nodes, traversing fully
# while n.nref is not None:	Second-last node	Finding the last node, inserting at end

# operation
class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None   # nref is next reference
        self.pref = None   # pref is previous reference

class DoublyLinkedList:

    def __init__(self):
        self.head=None

    def print_LL(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            n=self.head
            while n is not None:
                print(n.data,'-->',end=' ')
                n=n.nref
            print()

    def print_LL_reverse(self):
        if self.head is None:
            print('Linked list is empty')
            return
        else:
            n=self.head
            while n.nref is not None:   #to goto last node
                n=n.nref
            while n is not None:
                print(n.data,'-->',end=' ')
                n=n.pref   # to print from last node to first node
        print()
    # Doubly linked list operations

    # 1.When linked list is empty
    def insert_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print('Linked List is not empty !')
            return

    # 2.inserting at beginning LL is not empty and LL is empty.
    def add_begin(self,data):
        new_node=Node(data)
        if self.head is None:
           self.head=new_node
           return
        else:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node

    # adding node at end of LL
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        else:
            n=self.head
            while n.nref is not None:  # Traverse to the last node
                n=n.nref
            n.nref=new_node
            new_node.pref=n

    # adding before and after a node in a linked list
    def add_after(self,data,x):
        if self.head is None:
            print('LL is empty !')
            return
        else:
            n=self.head
# Note: here the while loop come out of loop at two conditions if get satisfied 1.when no x is matched 2.when x is matched
            while n is not None:
                if x==n.data:  # Stop if the matching node is found
                    break
                n=n.nref
            if n is None:
                print('Given Node is not present in DDL ')
            else:
                new_node=Node(data)
                new_node.nref=n.nref
                new_node.pref=n
                if n.nref is not None: # If not the last node, update the next node's `pref`  # checking if it is not the last node , as if it is last node then three condition is enough 
                    n.nref.pref=new_node
                n.nref=new_node


    def add_before(self,data,x):
        if self.head is None:
            print('LL is empty !')
        else:
            n=self.head
# Note: here the while loop come out of loop at two conditions if get satisfied 1.when no x is matched 2.when x is matched
            while n is not None:
                if x==n.data:
                    break
                n=n.nref
            if n is None:
                print('Given Node is not present in DDL ')
            else:
                new_node=Node(data)
                # rest then first node k badd addition
                new_node.nref=n
                new_node.pref=n.pref
                if n.pref is not None:   # if n is not first node
                    n.pref.nref=new_node
                else:  # if n is first node
                    self.head=new_node
                n.pref=new_node


    # deletion operations

    def delete_begin(self):
        if self.head is None:
            print('LL is empty !')
            return
            # check if only one node is there
        if self.head.nref is None:
            self.head=None
            return
            # rest cases when more than one node is there
        self.head=self.head.nref
        self.head.pref=None

    def delete_end(self):
        if self.head is None:
            print('LL is empty !')
            return
        
        # Check if there is only one node
        if self.head.nref is None:
            self.head=None
            return
        
        # rest cases when more than one node is there
        # Traverse to the last node
        n=self.head
        while n.nref is not None:
            n=n.nref
    
        # Update second-last node's next reference to None
        n.pref.nref=None
    

# Delete by value
    def delete_by_value(self,x):
        # check if Dll is empty
        if self.head is None:
            print('DLL is empty can\'t delete it')
            return
        
        # check if there is only one node
        if self.head.nref is None:
            if x==self.head.data:
                self.head=None
            else:
                print('X is not present in Dll')
            return
        #  deleting first node
        if self.head.data==x:
            self.head=self.head.nref
            self.head.pref=None
            return
        #  Traverse the DLL to find the node, and delete it if found 
        n=self.head
        while n.nref:
            if n.data==x:
                break
            n=n.nref
        if n.nref!=None:
            n.nref.pref=n.pref
            n.pref.nref=n.nref
        else:
            if n.data==x:
                n.pref.nref=None
            else:
                print('X is not present in Dll')
                return

            


dl1=DoublyLinkedList()

# dl1.insert_empty(10)
# dl1.insert_empty(10)
# dl1.add_begin(20)
# dl1.add_end(90)

""" dl1.add_begin(10)
dl1.add_after(20,10) """

# dl1.add_begin(10)
# dl1.add_end(20)
# dl1.add_end(30)
# dl1.delete_end()

dl1.print_LL()
print()
dl1.print_LL_reverse()


