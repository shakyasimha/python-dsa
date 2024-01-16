from linked_list.linkedlist import LinkedList

## Main function goes here
def main():
    list1 = LinkedList()
    
    for i in range(0,10):
        list1.insert(i)
        
    list1.display()

if __name__ == "__main__":
    main()