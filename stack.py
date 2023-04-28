## Implementing a stack 

## Node class here
class Node: 
    def __init__(self, data, next):
        self.data = data 
        self.next = next 

## Stack class here
class Stack:
    ## Constructor 
    def __init__(self):
        ## tos = Top of Stack
        self.tos = None 
    
    ## Pushing the elements to TOS
    def push(self, data):
        new_node = Node(data, None)

        if self.tos is not None: 
            new_node.next = self.tos 
    
        self.tos = new_node

    
    ## Popping the elements off the stack
    def pop(self):
        try: 
            if self.tos.next is None:
                self.tos = None 

            self.tos = self.tos.next 
        except Exception as e:
            if self.tos is None:
                print("Stack underflow")


    ## Returns TOS 
    def top(self):
        return self.tos.data
    

    ## Displaying the entire stack
    def print_stack(self):
        if self.tos is None:
            print("Stack empty")
        else:
            curr_node = self.tos

            while curr_node: 
                print(f"{curr_node.data} ")
                curr_node = curr_node.next 