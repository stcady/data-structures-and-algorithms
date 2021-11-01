from collections import deque

# Stack implementation using one single list
class TwoStack():

    # Stack class constructor method
    def __init__(self):
        self.data = deque([])
        self.size1 = 0
        self.size2 = 0

    # push appends a value to the first stack
    # enqueues element to left side or queue
    def stack_push1(self, value):
        self.data.appendleft(value)
        self.size1 += 1

    # push appends a value to the second stack
    # enqueues element to right side of queue
    def stack_push2(self, value):
        self.data.append(value)
        self.size2 += 1

    # pop pops the value from the first stack and returns it
    # dequeues element from left side of queue
    def stack_pop1(self):
        if self.size1 == 0:
            raise RuntimeError("StackEmptyException")
        self.size1 -= 1
        return self.data.popleft()

    # pop pops the value from the second stack and returns it
    # dequeues element from right side of queue
    def stack_pop2(self):
        if self.size2 == 0:
            raise RuntimeError("StackEmptyException")
        self.size2 -= 1
        return self.data.pop()

def main():
    s = TwoStack()
    i = 0
    while i < 10:
        s.stack_push1(i)
        i += 1
    j = 0
    while j < 10:
        s.stack_push2(j + 10)
        j += 1
    k = 0
    while k < 10:
        print()
        print(s.data)
        print("stack one pop: ", s.stack_pop1())
        print("stack two pop: ", s.stack_pop2())
        k += 1

if __name__ == "__main__":
    main()