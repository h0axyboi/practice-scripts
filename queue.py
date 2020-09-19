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
