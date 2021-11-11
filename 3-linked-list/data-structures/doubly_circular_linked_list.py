class CircularDoublyLinkedList(object):

    # Node class representing elements of linked list
    class Node:

        # Node class constructor for creating a new node
        def __init__(self, v, n=None, p=None):
            self.value = v
            self.next = n
            self.prev = p

    # LinkedList class constructur for creating a new circular list
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # add_head inserts new node with the value passed at the head of the curcular list
    def add_head(self, value):
        new_node = self.Node(value, None, None)
        self.size += 1
        if self.head == None:
            self.tail = self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.head.prev
            self.head.prev = new_node
            self.head = new_node

    # add_tail inserts new node with value passed at the end of the circular list
    def add_tail(self, value):
        new_node = self.Node(value, None, None)
        self.size -= 1
        if self.head == None:
            self.head = self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.tail.next
            new_node.prev = self.tail
            self.tail.next = new_node
            new_node.next.prev = new_node
            self.tail = new_node
    
    # remove_head deletes the first node in the circular list
    def remove_head(self):
        if self.head == None:
            raise RuntimeError("EmptyListException")
        self.size -= 1
        value = self.head.value
        if self.head == self.head.next:
            value = self.head.value
            self.head = None
            self.tail = None
            return value
        next_node = self.head.next
        next_node.prev = self.tail
        self.tail.next = next_node
        self.head = next_node
        return value

    # remove_tail deletes the last node in the circualr list
    def remove_tail(self):
        if self.tail == None:
            raise RuntimeError("EmptyListException")
        self.size -= 1
        value = self.tail.value
        if self.tail == self.tail.next:
            self.head = None
            self.tail = None
            return value
        prev = self.tail.prev
        prev.next = self.head
        self.head.prev = prev
        self.tail = prev
        return value

    # free deletes all nodes in the list
    def free(self):
        self.tail = None
        self.head = None
        self.size = 0

    # is_present searches the circular list to find the provided value
    def is_present(self, data):
        temp = self.tail
        i = 0
        while i < self.size():
            if temp.value ==  data:
                return True
            temp = temp.next
            i += 1
        return False

    # print_list prints the values in the circluar list
    def print_list(self):
        if self.is_empty():
            return
        temp = self.tail.next
        while temp != self.tail:
            print(temp.value, end=' ')
            temp = temp.next
        print(temp.value, end=' ')