## Class for Node here
class Node: 
    def __init__(self, data=None):
        self.data = data 
        self.next = None 


## Class for Linked List here
class LinkedList: 
    ## Constructor
    def __init__(self):
        self.head = Node(None)

    ## Returns the size of the list
    def size(self):
        count = 0
        curr_node = self.head 

        while curr_node: 
            count += 1
            curr_node = curr_node.next

        return count


    ## For inserting the data
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            # If the head is null, then the new node becomes the head
            self.head = new_node
        else:
            curr_node = self.head

            # Traversing the node till next node
            while curr_node.next is not None:
                curr_node = curr_node.next 

            curr_node.next = new_node


    ## Prepending the list - adding an element ahead of the node
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head 
        self.head = new_node


    ## Insert node at a position (indexing start at 0)
    def insert_at(self, data, pos):
        curr_node = self.head
        new_node = Node(data)
        count = 0

        if pos == 0:
            new_node.next = self.head 
            self.head = new_node
            return 
        
        while curr_node and count != pos:
            curr_node = curr_node.next 
            pos += 1

        new_node.next = curr_node.next.next 
        curr_node.next = new_node 


    ## Pops the last element in the list
    def pop(self):
        curr_node = self.head

        while curr_node.next.next is not None:
            curr_node = curr_node.next 

        curr_node.next = None



    ## Returns the element at an index
    def at(self, idx):
        try:
            curr_node = self.head
                
            for i in range(0, idx): 
                curr_node = curr_node.next 

            return curr_node.data

        except Exception as e:
            if self.head is None:
                return -1
    

    ## For printing the entire list
    def print_list(self):
        if self.head is None:
            print("The list is empty.")
        else: 
            curr_node = self.head.next

            while curr_node: 
                print(f"{curr_node.data}")
                curr_node = curr_node.next


