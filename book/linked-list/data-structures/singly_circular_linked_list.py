class CircularLinkedList(object):

    # Node class representing elements of linked list
    class Node:

        # Node class constructor for creating a new node
        def __init__(self, v, n=None):
            self.value = v
            self.next = n

    # LinkedList class constructur for creating a new circular list
    def __init__(self):
        self.tail = None
        self.size = 0

    # is_empty checks if the circular list is empty
    def is_empty(self):
        if self.tail == None:
            return True
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

    # add_head inserts new node with the value passed at the head of the curcular list
    def add_head(self, value):
        temp = self.Node(value, None)
        self.size += 1
        if self.tail == None:
            self.tail = temp
            temp.next = temp
        else:
            temp.next = self.tail.next
            self.tail.next = temp
    
    # add_tail inserts new node with value passed at the end of the circular list
    def add_tail(self, value):
        temp = self.Node(value, None)
        self.size += 1
        if self.tail == None:
            self.tail = temp
            temp.next = temp
        else:
            temp.next = self.tail.next
            self.tail.next = temp
            self.tail = temp

    # remove_head deletes the first node in the circular list
    def remove_head(self):
        if self.is_empty():
            raise RuntimeError("EmptyListException")
        self.size -= 1
        value = self.tail.next.value
        if self.tail == self.tail.next:
            self.tail = None
        else:
            self.tail.next = self.tail.next.next
    
    # delete_node deletes the first node of a provided value
    def delete_node(self, del_value):
        if self.is_empty():
            return False
        curr = self.tail.next
        head = self.tail.next
        if curr.value == del_value:
            if curr == curr.next:
                self.tail = None
            else:
                self.tail.next = self.tail.next.next
        prev = curr
        curr = curr.next
        while curr.next != head:
            if curr.value == del_value:
                if curr == self.tail:
                    self.tail = prev
                prev.next = curr.next
                return True
            prev = curr
            curr = curr.next
        return False

    # free deletes all nodes in the list
    def free(self):
        self.tail = None
        self.size = 0

    # copy_list_reversed copies the list reversed to a new list
    def copy_list_reversed(self):
        cl = CircularLinkedList()
        curr = self.tail.next
        head = curr
        if curr != None:
            cl.add_head(curr.value)
            curr = curr.next
        while curr != head:
            cl.add_head(curr.value)
            curr = curr.next
        return cl

    # copy_list copies the list to a new list
    def copy_list(self):
        cl = CircularLinkedList()
        curr = self.tail.next
        head = curr
        if curr != None:
            cl.add_tail(curr.value)
            curr = curr.next
        while curr != head:
            cl.add_tail(curr.value)
            curr = curr.next
        return cl