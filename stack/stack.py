class Node:
    """
        Node class goes here
    """
    def __init__(self, data=None):
        self.data = data 
        self.next = None

class Stack: 
    """
        Stack class goes here
    """
    def __init__(self):
        ## ctor 
        self.tos = None 
        self.size = 0 
        
    def sizeof(self):
        ## Returns size of stack
        return self.size 
    
    def is_empty(self):
        ## Returns if stack is empty or not
        return self.tos == None 
    
    def push(self, data):
        ## Pushing data from stack
        new_node = Node(data)
        
        if not self.is_empty():
            new_node.next = self.tos 
        
        self.tos = new_node
        self.size += 1
        
    def pop(self):
        ## Popping data from stack
        if self.is_empty(): 
            print("Stack underflow")
            return -1
        else: 
            ## Retrieve data from TOS 
            ## Then pop out the TOS by pointing TOS to the next element in stack
            pop_data = self.tos.data
            self.tos = self.tos.next
            
            self.size -= 1
            return pop_data
   
    def top(self):
        ## Returns top of the stack
        if self.is_empty(): 
            print("Stack empty")
            return -1 
        else: 
            return self.tos.data 
        
        
    def show(self):
        ## Print the entire stack
        if not self.is_empty():
            print(f"{self.tos.data} -> TOS")
            temp = self.tos.next 
            
            while temp is not None: 
                print(f"{temp.data}")
                temp = temp.next
                
            print(f"Size of stack: {self.size}")