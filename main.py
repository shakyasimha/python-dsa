from linked_list.linkedlist import LinkedList
from time import time 


## Main function goes here
def main():
    start_time = time()
    
    list1 = LinkedList()
    
    for i in range(0,10):
        list1.insert(i)
        
    list1.display()
    
    end_time = time()
    elapsed_time = end_time - start_time 
    print(f"Time to execute: {elapsed_time}")

if __name__ == "__main__":
    main()