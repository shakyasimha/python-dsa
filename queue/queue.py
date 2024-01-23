"""
    Implementing queue in Python
"""

class Node:
    """
        Node class
    """
    def __init__(self, data):
        ## ctor
        self.data = data
        self.next = None

class Queue:
    """
        Queue class
    """
    def __init__(self):
        ## ctor
        self.head = None
        self.tail = None
        self.size = 0
       
    def is_empty(self):
        """ Checking if the queue is empty """
        return self.head is None
     
    def enque(self, data):
        """ Method for adding data to queue """
        new_node = Node(data)
        
        try:   
            if self.is_empty():
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = self.tail.next
                
            self.size += 1
        except Exception as e:
            return str(e)
            
    def deque(self):
        """ Method for removing data from queue """
        try: 
            deque_data = self.head.data
            self.head = self.head.next
            self.size -= 1
            
            return deque_data
        except Exception as e:
            return str(e)
        
        
    def show(self):
        """ Displaying the entire queue """
        try: 
            if self.is_empty():
                print("Queue empty")
            else: 
                temp_node = self.head 
                output_str = ""
                
                while temp_node is not None: 
                    output_str += str(temp_node.data) + "->"
                    temp_node = temp_node.next 
                
                output_str = output_str[:-2]  # Removing the last arrow
                print(output_str)
                print(f"Size of queue: {self.size}")
        except Exception as e:
            return str(e)
            
        