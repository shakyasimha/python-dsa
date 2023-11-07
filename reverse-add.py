## Add 1 to a number represented by linked list
## 
## Problem statement
## Number is represented in Linked List such that each digit corresponds to a node in the linked list.
## Add 1 to it. For example, if 1999 is represented as 1->9->9->9, adding 1 to it should turn it into 2->0->0->0

## How to solve this:
## 1. Reverse the linked list
## 2. Traverse from left to right of the reversed list and keep adding 1. If there is a carry, move to next node.
## 3. Reverse the list and return head.


## Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 


## Function for appending the list
def append(head, data):
    new_node = Node(data)
    curr_node = head 

    if curr_node is None: 
        curr_node = new_node 
    else:
        ## Node traversal
        while curr_node.next is not None:
            curr_node = curr_node.next 

        curr_node.next = new_node 

    return head


## Function for reversing the list
def reverse(head):
    current = head 
    prev, next = None, None

    while current: 
        next = current.next 
        current.next = prev 
        prev = current 
        current = next 

    return prev 


## Function for displaying the list 
def display(head):
    try:
        current = head 

        while current: 
            print(f"{current.data}->", end='')
            current = current.next 

    except Exception as e: 
        print("Empty list")

    print()


## Function for breaking down the number and inserting each digit to the list 
def insert_digits(head, number):
    remain = 0

    while number != 0:
        remain = number%10
        number  = number/10

        head = append(head, remain)

    return head 


## Main function called here  
def main():
    head = Node(None) 

    num_input = int(input("Enter a number: "))
    print(f"Original input number: {num_input}")

    head = insert_digits(head, num_input)
    print(f"Number in a list form: {display(head)}")

if __name__ == "__main__":
    main()