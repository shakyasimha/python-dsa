## Doubly linked list

## Node class
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
        
## Doubly linked list class
class DoubleList:
    def __init__(self):
        