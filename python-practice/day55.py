# Question: Day 55: Implement stack data structure with push/pop/peek methods.
class Stack:
    def __init__(self):
        self._items = []
    
    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        return self._items.pop() if not self.is_empty() else None
    
    def peek(self):
        return self._items[-1] if not self.is_empty() else None
    
    def is_empty(self):
        return len(self._items) == 0
    
    def size(self):
        return len(self._items)

s = Stack()
s.push(1)
s.push(2)
print(s.pop())  # 2
