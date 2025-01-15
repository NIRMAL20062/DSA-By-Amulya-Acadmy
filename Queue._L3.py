# Queue from emptylist

""" queue=[]
queue.append(1)
queue.append(11)
queue.append(111)
print(queue)
queue.pop(0)
queue.pop(0)
queue.pop(0)
print(queue) """


""" queue=[]
queue.insert(0,1)
queue.insert(0,11)
queue.insert(0,111)
print(queue)
queue.pop()
print(queue)
queue.pop()
print(queue)
queue.pop()
print(queue) """

""" queue=[]
if not queue:
    print('b')
 """

""" queue=[]
def enqueue():
    element=input('Enter: ')
    queue.append(element)
    print(element,'is added to queue! ')
def dequeue():
    if not queue:
        print('Queue is empty')
    else:
        e=queue.pop(0)
        print('removed element: ' ,e)
def display():
    print(queue)
while True:
    print('Select the operation 1.add 2.remove 3.show 4.quit')
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print('Choose correct operations') """


# implementation using module classes 
""" import collections
q=collections.deque()
print(q)
q.appendleft(1)
print(q)
q.appendleft(2)
print(q)
q.appendleft(3)
print(q)
q.pop()
print(q)
q.pop()
print(q)
q.pop()
print(q) """


""" import collections
q=collections.deque()
print(q)
q.append(1)
print(q)
q.append(2)
print(q)
q.append(3)
print(q)
q.popleft()
print(q)
q.popleft()
print(q)
q.popleft()
print(q) """


""" import queue
q=queue.Queue()
q.put(1)
print(q)
q.put(2)
print(q)
q.put(3)
print(q)
x=q.get()
print(x)
x=q.get()
print(x)
x=q.get()
print(x)
x=q.get()
print(x) """

# after 5 sec queue full message appears
""" import queue
q=queue.Queue(1)
q.put(1,block=True,timeout=5)
q.put(11,block=True,timeout=5)
print(q) """


# Here when q is full it will automatically show message 
""" import queue
q=queue.Queue(1)
q.put_nowait(1)
q.put_nowait(12)
print(q) """

# priority queue

# M-1
# by list 
""" q=[]
q.append(1)
print(q)
q.append(11)
print(q)
q.append(111)
q.sort()
print(q)
q.pop()
print(q)
q.pop()
print(q)
q.pop() """

# M-2

""" import queue
q=queue.PriorityQueue()
q.put(1)
q.put(2)
q.put(3)
q.put(3)
q.put(4)
print(q)
q.get()
print(q)
q.get()
print(q)
q.get()
print(q)
q.get()
print(q)
q.get()
print(q) """

""" q=[]
q.append((1,'A'))
q.append((3,'c'))
q.append((2,'b'))
print(q)
q.sort(reverse=True)
print(q)
q.sort(reverse=False)
print(q) """










 