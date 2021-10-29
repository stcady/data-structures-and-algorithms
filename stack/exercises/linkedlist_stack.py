# Stack implementation using linked list
class Stack:

    # Node subclass
    class Node:

        # Node class constructor method
        def __init__(self, v, n=None):
            self.value = v
            self.next = n

    # Stack class constructor method
    def __init__(self):
        self.head = None
        self.size = 0

    # is_empty checks if the stack is empty
    def is_empty(self):
        return (self.head == None)

    # size returns the number of elements in the stack
    def size(self):
        return self.size

    # print_stack prints the elements in the stack
    def print_stack(self):
        temp = self.head
        while temp != None:
            print(temp.value, end = ' ')
            temp = temp.next
    
    # peek returns the value stored in the top element of the stack
    def peek(self):
        if self.is_empty():
            raise RuntimeError("StackEmptyException")
        return self.head.value

    # push appends a value to the stack
    def push(self, value):
        self.head = self.Node(value, self.head)
        self.size += 1

    # pop pops the value from the stack and returns it
    def pop(self):
        if self.is_empty():
            raise RuntimeError("StackEmptyException")
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value

def main():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.pop()
    s.print_stack()

if __name__ == "__main__":
    main()