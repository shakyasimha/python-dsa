## Doubly linked list

class Node:
    def __init__(self, data=None):
        self.data = None
        self.prev = None
        self.next = None 

## Linked Lists class starts here
class DoubleList:
    def __init__(self):
        self.head = None 
        self.tail = None
        self.size = 0

    def is_empty(self):
        return (self.head == None)
    
    ## Append = add data to the end of the list
    def append(self, data):
        new_node = Node(data)

        if self.head is None: 
            self.head = new_node 
        else: 
            curr_node = self.head 

            while curr_node.next is not None: 
                curr_node = curr_node.next 

            curr_node.next = new_node 
            new_node.prev = curr_node 

    ## Prepend = add data to the front of the list
    def prepend(self, data):
        new_node = Node(data)

        # Case 1: when the list is empty
        # Case 2: when the list is not empty
        if self.head is None: 
            self.head = new_node 
        else: 
            ## What happens here:
            ## When a new node is to be prepended to the list, the next pointer of new node will point to the head of the list
            ## The prev pointer of head node will point to the new node
            ## Since the new node is added to the end of the list, the new node will become the head
            new_node.next = self.head 
            self.head.prev = new_node 
            self.head = new_node 

    ## Displaying the list
    def display(self):
        try:
            curr_node = self.head 

            while curr_node is not None: 
                print(f"{curr_node.data} ")
                curr_node = curr_node.next
                
        except Exception as e:
            print("Empty list")