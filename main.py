from queue.queue import Queue
from random import randint 

## Main function goes here
def main():
    queue = Queue()
    
    for i in range(0,15):
        data = randint(0,100)
        queue.enque(data)

    queue.show()
    
if __name__ == "__main__":
    main()