import time
import threading
from collections import deque

class Queue:
    def __init__(self):
        self.buffer=deque()
    def enqueue(self,data):
        self.buffer.appendleft(data)
    def dequeue(self):
        return self.buffer.pop()
    def is_empty(self):
        return len(self.buffer)==0
    def size(self):
        return len(self.buffer)

q=Queue()

def place(orders):
    for order in orders:
        q.enqueue(order)
        time.sleep(0.5)

def serve():
    time.sleep(1)
    while not q.is_empty():
        print(q.dequeue())
        time.sleep(2)

orders=['pizza','samosa','pasta','biriyani','burger']
t=time.time()
t1=threading.Thread(target=place,args=(orders,))
t2=threading.Thread(target=serve)
t1.start()
t2.start()
t1.join()
t2.join()
print('Time taken:',time.time()-t)
