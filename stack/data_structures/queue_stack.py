from collections import deque

# Stack implementation using a queue
class Stack(object):

    # Queue class constructor method
    def __init__(self):
        self.que1 = deque([])
        self.que2 = deque([])
        self.size = 0

    # add appends a value to the stack
    def push(self, value):
        self.que1.append(value)
        self.size += 1

    # pop removes a value from the top of the stack
    def pop(self):
        if self.is_empty():
            raise RuntimeError("QueueEmptyException")
        s = self.size
        value = None
        while s > 0:
            value = self.que1.popleft()
            if s > 1:
                self.que2.append(value)
            s -= 1
        self.que1, self.que2 = self.que2, self.que1
        self.size -= 1
        return value
            

    # is_empty checks if the stack is empty
    def is_empty(self):
        return self.size == 0

    # size returns the number of elements in the stack
    def size(self):
        return self.size

    # print_stack prints the elements in the stack
    def print_stack(self):
        if len(self.que1) > 0:
            i = len(self.que1) - 1
            while i >= 0:
                print(self.que1[i], end=' ')
                i -= 1
        print()
    

def main():
    s = Stack()
    s.push(1)
    s.push(11)
    s.push(111)
    s.print_stack()
    print(s.pop())
    print(s.pop())
    s.print_stack()

if __name__ == "__main__":
    main()