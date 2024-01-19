from stack.stack import Stack
from random import randint 

## Main function goes here
def main():
    stack = Stack()
    
    for i in range(0, 15):
        data = randint(0,100)
        stack.push(data)

    stack.show()
    
if __name__ == "__main__":
    main()