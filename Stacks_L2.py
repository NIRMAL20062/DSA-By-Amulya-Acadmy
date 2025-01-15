# reversing the string each charactr is pushed in and popped off which results in reversed string.

# to use stack in python we need to impliment it .
""" stack=[]
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack) """



# List se Stack
""" stack=[]
def push():
    element=input('Enter No.')
    stack.append(element)
    print(stack)
def pop_element():
    if not stack:
        print('Stack is empty!')
    else:
        e=stack.pop()
        print("removed element --> ",e)
        print(stack)
while True:
    print('Select the operation 1.Push 2.Pop 3.Quit ')
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print('Enter correct operation') """

# Module use krke
""" import collections   #in collections module a class called deque 
stack=collections.deque()
print(stack)
stack.append(1)
print(stack)
stack.append(2)
print(stack)
stack.append(3)
print(stack)
print(stack[-1])
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
if not stack:
    print('yes') """


""" import queue
stack=queue.LifoQueue(3)
stack.put(1)
stack.put(2)
stack.put(3)
print(stack)
stack.get()
print(stack) """

""" import queue
stack=queue.LifoQueue(3)
stack.put(1)
stack.put(2)
stack.put(3)
# stack.put(4,Timeout=1) """
















