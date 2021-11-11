# Queue implementation using a circular linked list
class Queue(object):

    # Node subclass
    class Node(object):

        # Node class constructor method
        def __init__(self, v, n=None):
            self.value = v
            self.next = n

    # Queue class constructor method
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # is_empty checks if the queue is empty
    def is_empty(self):
        return (self.head == None)

    # size returns the number of elements in the queue
    def size(self):
        return self.size

    # print_queue prints the elements in the queue
    def print_queue(self):
        temp = self.head
        while temp != None:
            print(temp.value, end = ' ')
            temp = temp.next

    # peek returns the value stored in the top element of the queue
    def peek(self):
        if self.is_empty():
            raise RuntimeError("QueueEmptyException")
        return self.head.value

    # add enqueues an element to the queue
    def add(self, value):
        temp = self.Node(value, None)
        self.size += 1
        if self.head == None:
            self.head = self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp

    # remove dequeues an element from the queue
    def remove(self):
        if self.is_empty():
            raise RuntimeError("QueueEmptyException")
        self.size -= 1
        value = self.head.value
        self.head = self.head.next
        return value

def main():
    que = Queue()
    i = 1
    while i <= 100:
        que.add(i)
        i += 1
    i = 1
    que.print_queue()
    print()
    while i <= 50:
        if not que.is_empty():
            print(que.remove())
        else:
            print("queue is empty")
            break
        i += 1
    que.print_queue()
    print()

if __name__ == "__main__":
    main()