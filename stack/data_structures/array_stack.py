# Stack implementation using array
class Stack(object):

    # Stack class constructor method
    def __init__(self):
        self.data = []

    # is_empty checks if the stack is empty
    def is_empty(self):
        return (len(self.data) == 0)

    # size returns the number of elements in the stack
    def size(self):
        return len(self.data)

    # print_stack prints the elements in the stack
    def print_stack(self):
        print(self.data)

    # push appends a value to the stack
    def push(self, value):
        self.data.append(value)
    
    # pop pops the value from the stack and returns it
    def pop(self):
        if self.is_empty():
            raise RuntimeError("StackEmptyException")
        return self.data.pop()

    # top returns the value stored in the top element of the stack
    def top(self):
        if self.is_empty():
            raise RuntimeError("StackEmptyException")
        return self.data[len(self.data) - 1]

def main():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.pop()
    s.print_stack()

if __name__ == "__main__":
    main()