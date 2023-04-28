## Implementing a queue 


## Node class here
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

## Queue class starts here
class Queue:
    def __init__(self):
        self.head = None 
        self.tail = None
        self.size = 0
    
    ## Returns the queue size
    def sizeof(self):
        return self.size 
    

    ## For appending element on the list
    def enque(self, data):
        curr_node = Node(data)

        if self.head is None:
            self.head = curr_node
            self.tail = curr_node
        else:
            self.tail.next = curr_node 
            self.tail = curr_node

        self.size += 1
        
    ## For removing data off the queue
    def deque(self):
        if self.sizeof() == 0:
            return IndexError("Empty queue")

        # Return the item, and remove the item from the queue
        item = self.head.data
        self.head = self.head.next
        self.size -= 1

        return item