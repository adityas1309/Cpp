# Question: Day 46: Implement a queue data structure using collections.deque.
from collections import deque

class Queue:
    def __init__(self):
        self._items = deque()
    
    def enqueue(self, item):
        self._items.append(item)
    
    def dequeue(self):
        return self._items.popleft() if not self.is_empty() else None
    
    def is_empty(self):
        return len(self._items) == 0
    
    def size(self):
        return len(self._items)

# Usage
q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # 1
