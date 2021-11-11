from collections import deque

# Queue implementation using python deque class
class Queue(object):

    # Queue class constructor method
    def __init__(self):
        self.data = deque([])

    # add appends a value to the queue
    def add(self, value):
        self.data.append(value)

    # remove removes a value from the front of the queue
    def remove(self):
        value = self.data.popleft()
        return value

    # is_empty hecks if the queue is empty
    def is_empty(self):
        return len(self.data) == 0

    # size returns the number of elements in the queue
    def size(self):
        return len(self.data)

    # print_queue prints the elements in the queue
    def print_queue(self):
        print(self.data)

def main():
    que = Queue()
    i = 0
    while i < 20:
        que.add(i)
        i += 1
    que.print_queue()
    i = 0
    while i < 22:
        if not que.is_empty():
            print(que.remove())
        else:
            print("queue is empty")
            break
        i += 1
    que.print_queue()

if __name__ == "__main__":
    main()