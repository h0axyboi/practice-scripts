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

def get_binary(n):
    q=Queue()
    q.enqueue('1')
    binaries=['0','1']
    for i in range(n):
        x=q.dequeue()
        print(x)
        for thing in binaries:
            q.enqueue(x+thing)

if __name__=='__main__':
    get_binary(21)
