from random import randint 
from queue.queue import Queue
# import sys 

## Main function goes here
def main():
    queue = Queue()
    
    for i in range(0,15):
        data = randint(0,100)
        queue.enque(data)
 
    queue.show()
    # print(sys.path)
    
if __name__ == "__main__":
    main()