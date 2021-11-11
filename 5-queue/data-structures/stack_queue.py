# Queue implementation using a stack
class Queue(object):

    # Queue class constructor method
    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    # add appends a value to the queue
    def add(self, value):
        self.stk1.append(value)

    # remove removes a value from the front of the queue
    def remove(self):
        if self.is_empty():
            raise RuntimeError("QueueEmptyException")
        if len(self.stk2) != 0:
            return self.stk2.pop()
        while len(self.stk1) != 0:
            self.stk2.append(self.stk1.pop())
        return self.stk2.pop()

    # is_empty checks if the queue is empty
    def is_empty(self):
        return (len(self.stk1) + len(self.stk2)) == 0

    # size returns the number of elements in the queue
    def size(self):
        return (len(self.stk1) + len(self.stk2))

    # print_queue prints the elements in the queue
    def print_queue(self):
        if len(self.stk2) != 0:
            i = len(self.stk2) - 1
            while i >= 0:
                print(self.stk2[i], end=' ')
                i -= 1
        if len(self.stk1) != 0:
            i = len(self.stk1) - 1
            while i >= 0:
                print(self.stk1[i], end=' ')
                i -= 1
        print()

def main():
    que = Queue()
    que.add(1)
    que.add(11)
    que.add(111)
    que.print_queue()
    print(que.remove())
    print(que.remove())
    que.print_queue()

if __name__ == "__main__":
    main()