## Implementing a doubly linked list

## Node class 
class Node:
    def __init__(self, data):
        self.data = data 
        self.prev = None 
        self.next = None 
        
        
## Double linked list class
class DoubleList:
    def __init__(self):
        self.head = None 
        
    """
        Methods:
        
        - append 
        - insert at nth index
        - removing end node
        - removing nth node 
        - removing head
        - prepending
        - size
        - is_null
    """
    ## Checks if the list is null
    def is_null(self):
        return self.head is None 
    
    ## Returns size of node
    def sizeof(self):
        size = 0 
        curr = self.head 
        
        while curr is not None:
            size+=1 
            curr = curr.next 
        
        return size
        
    ## Appends aka adds at end of the list
    def append(self, data):
        new_node = Node(data)

        if self.is_null():
            self.head = new_node 
        else:
            curr_node = self.head 
            
            while curr_node is not None:
                curr_node = curr_node.next 
                
            curr_node.next = new_node 
            new_node.prev = curr_node 
            curr_node = new_node 
            
    ## Insert at nth index 
    def insert(self, data, idx):
        new_node = Node(data)
        
        if self.is_null():
            self.head = new_node 
        else: 
            curr_node = self.head 
            
            for i in range(0,idx):
                curr_node = curr_node.next 
                
            curr_node.next = new_node 
            new_node.prev = curr_node 
            curr_node = new_node 
    
    ## Remove the end node
    def pop(self):
        curr_node = self.head 
        
        while curr_node.next.next is not None: 
            curr_node = curr_node.next 
            
        curr_node.next = None 
        
    ## Remove element from nth index
    def remove(self, idx):
        try:
            curr_node = self.head
            
            for i in range(0,idx):
                curr_node = curr_node.next 
                
            """
                Next node should point to previous node and previous node should point to next node
                Current node gets purged
            """
            curr_node.prev.next = curr_node.next 
            curr_node.next.prev = curr_node.prev 
            
        except Exception as e:
            return str(e)
        