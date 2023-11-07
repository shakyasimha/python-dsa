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
        Functions/methods involved in linked list:
        - insert
        - append at nth position
        - remove at nth position
        - add at head
        - pop (remove latest node)
        - traverse and print
    """
    
    ## Checking if the list is null
    def is_null(self):
        return (self.head is None)
    
    
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
    def append(self, data, pos):
        new_node = Node(data)
        
        if self.is_null():
            self.head = new_node 
        else: 
            temp = self.head 
            i = 0
            
            while i < pos: 
                temp = temp.next 
                i += 1
                
            new_node.next = temp.next 
            temp.next = new_node 
            
            
    ## Pop the elements 
    def pop(self):
        try: 
            temp_node = self.head 
            
            while temp_node.next.next is not None: 
                temp_node = temp_node.next 
                
            temp_node.next = None 
        except Exception as e:
            return str(e)   
    
    
    ## Remove element at nth position
    def remove(self, pos):
        try: 
            temp_node = self.head 
            i = 0 
            
            while i < pos: 
                temp_node = temp_node.next 
                i += 1
                
            temp_node.next = temp_node.next.next 
        except Exception as e:
            return str(e)
        
        
    ## Add element at head
    def add_head(self, data):
        new_node = Node(data)
        
        if self.is_null(): 
            self.head = new_node 
        else: 
            new_node.next = self.head
            self.head = new_node 
            
            
    ## Remove element from head 
    def remove_head(self, data):
        try: 
            self.head = self.head.next 
        except Exception as e:
            return str(e)
        
        
    ## Print linked list 
    def display(self):
        if self.is_null():
            print("Empty list")
        else: 
            temp_node = self.head 
            
            while temp_node is not None: 
                print(f"{temp_node.data} -> ")
                temp_node = temp_node.next 
                
                
    ## Return size of the linked list
    def sizeof(self):
        if self.is_null():
            return 0 
        else: 
            size = 0 
            temp_node = self.head 
            
            while temp_node is not None: 
                size+=1 
                temp_node = temp_node.next 
                
