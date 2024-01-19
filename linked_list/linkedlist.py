## Singly linked list implementation
from time import time 

## Node class
class Node: 
    def __init__(self, data=None):
        self.data = data 
        self.next = None
        
        
## Linked List class
class LinkedList:
    ## Constructor
    def __init__(self):
        self.head = Node()
        self.time_elapsed = 0
    """
        All the operations in this linked list:
        
        - is_null -> checks if the list is null
        - insert -> inserting at the end of the list
        - append -> appends a node at nth index
        - pop -> remove node from the end of the list 
        - remove -> removes node from the nth index
        - prepend -> add element at the start
        - remove_head -> remove head 
        - find -> finds if the element exists
        - at -> returns element given index 
        - display -> print an entire list
    """
    ## Checking if the list is null
    def is_null(self):
        return (self.head == None)
    
    ## Return size of the linked list
    def sizeof(self):
        size = 0 

        if not self.is_null():
            curr_node = self.head 
            while curr_node is not None: 
                size+=1 
                curr_node = curr_node.next 
        
        return size
    
    ## Inserting the linked list
    def insert(self, data):
        new_node = Node(data)
        
        if self.is_null():
            self.head = new_node
        else: 
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node 
            
    ## Appending the linked list 
    def append(self, data, idx):
        new_node = Node(data)
        
        if self.is_null():
            self.head = new_node 
        else: 
            temp = self.head 
            i = 0
            while i < idx: 
                temp = temp.next 
                i += 1 
            new_node.next = temp.next 
            temp.next = new_node 
    
    ## Pop the elements 
    def pop(self):
        if self.is_null():
            return "Empty list"
        elif self.head.next is None:
            self.head = None 
        else: 
            curr_node = self.head 
            while curr_node.next.next is not None:
                curr_node = curr_node.next 
            curr_node.next = None
    
    
    ## Remove element at nth index
    def remove(self, idx):
        if self.is_null():
            return "Empty list"
        elif idx == 0:
            self.head = self.head.next 
        else:
            curr_node = self.head
            i = 0 
            
            while i < idx: 
                curr_node = curr_node.next 
                i+=1

            if curr_node.next is not None:
                curr_node.next = curr_node.next.next 
                
    ## Add element at head
    def prepend(self, data):       
        new_node = Node(data)
        
        if self.is_null(): 
            self.head = new_node 
        else: 
            new_node.next = self.head
            self.head = new_node 
            
    ## Remove element from head 
    def remove_head(self):
        self.head = self.head.next 
        
         
    ## Search for an element in the list 
    def find(self, data):        
        try: 
            curr_node = self.head 
            idx = 0 
            
            while curr_node is not None:
                if curr_node.data == data: 
                    break
                
                curr_node = curr_node.next 
                idx += 1 
                
            return idx
        except:
            return -1 
        
        
    ## Returns an element at an index
    def at(self, idx):
        try: 
            curr_node = self.head 
            
            for i in range(0,idx):
                curr_node = curr_node.next 
                
            return curr_node.data 
        except:
            return None
        
    ## Reverse a linked list 
    def reverse(self):
        try:
            prev = None
            next = None 
            curr = self.head 
            
            while curr is not None: 
                next = curr.next 
                curr.next = prev 
                prev = curr 
                curr = next 
        except:
            return None 
            
    ## Print linked list 
    def display(self):
        if self.is_null():
            print("Empty list")
        else: 
            curr_node = self.head 
            final_exp = ""
            
            while curr_node is not None: 
                final_exp += str(curr_node.data) + "->"
                curr_node = curr_node.next 
            
            final_exp = final_exp[:-2]  
            print(final_exp)
                
                
        
