## Singly linked list implementation

## Node class
class Node: 
    def __init__(self, data=None):
        self.data = data 
        self.next = None
        
        
## Linked List class
class LinkedList:
    ## Constructor
    def __init__(self):
        self.head = None 
    
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
        return (self.head is None)
    
    ## Return size of the linked list
    def sizeof(self):
        if self.is_null():
            return 0 
        else: 
            size = 0 
            curr_node = self.head 
            
            while curr_node is not None: 
                size+=1 
                curr_node = curr_node.next 
                
    
    ## Inserting the linked list
    def insert(self, data):
        new_node = Node(data)
        
        if self.head == None:
            self.head = new_node
        else: 
            temp = self.head
            
            while temp is not None:
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
            
            for i in range(0,idx): 
                temp = temp.next 
                
            new_node.next = temp.next 
            temp.next = new_node 
            
            
    ## Pop the elements 
    def pop(self):
        try: 
            curr_node = self.head 
            
            while curr_node.next.next is not None: 
                curr_node = curr_node.next 
                
            curr_node.next = None 
        except Exception as e:
            return str(e)   
    
    
    ## Remove element at nth index
    def remove(self, idx):
        try: 
            curr_node = self.head 
            i = 0 
            
            for i in range(0,idx): 
                curr_node = curr_node.next 
                
            curr_node.next = curr_node.next.next 
        except Exception as e:
            return str(e)
        
        
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
        try: 
            self.head = self.head.next 
        except Exception as e:
            return str(e)
        
        
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
            
            while curr_node is not None: 
                print(f"{curr_node.data} -> ")
                curr_node = curr_node.next 
                
                
        
