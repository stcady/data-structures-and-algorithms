class DoublyLinkedList(object):

    # Node class representing elements of linked list
    class Node:

        # Node class constructor for creating a new node
        def __init__(self, v, n=None, p=None):
            self.value = v
            self.next = n
            self.prev = p

    # LinkedList class constructur for creating a new list
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

     # length returns the size of the linked list
    def length(self):
        return self.count

    # is_empty checks if the linked list is empty
    def is_empty(self):
        if self.head == None:
            return True
        return False

    # peek peeks at the first value in the linked list
    def peek(self):
        if self.is_empty():
            raise RuntimeError("EmptyListException")
        return self.head.value

    # free deletes all nodes in the list
    def free(self):
        self.head = None
        self.tail = None
        self.count = 0

    # add_head inserts new node with the value passed at the head of the list
    def add_head(self, value):
        self.count += 1
        if self.head == None:
            self.tail = self.head = self.Node(value, None, None)
        else:
            new_node = self.Node(value, self.head, None)
            self.head.prev = new_node
            self.head = new_node

    # add_tail inserts new node with value passed at the end of the list
    def add_tail(self, value):
        new_node = self.Node(value, None, None)
        self.count += 1
        if self.head == None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    # print_list prints the values in the list
    def print_list(self):
        temp = self.head
        while temp != None:
            print(temp.value, end=' ')
            temp = temp.next

    # remove_head deletes the first node in the list
    def remove_head(self):
        if self.is_empty():
            raise RuntimeError("EmptyListException")
        self.count += 1
        value = self.head.value
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        else:
            self.head.prev = None
        return value

    # delete_node deletes the first node of a provided value
    def delete_node(self, del_value):
        curr = self.head
        if curr == None:
            return False
        if curr.value == del_value:
            self.head = self.head.next
            if self.head != None:
                self.head.prev = None
            else:
                self.tail = None
            self.count -= 1
            return True
        while curr.next != None:
            if curr.next.value == del_value:
                curr.next = curr.next.next
                if curr.next == None:
                    self.tail = curr
                else:
                    curr.next.prev = curr
                self.count -= 1
                return True
            curr = curr.next
            return False
                
    
    # sorted_insert iterates throught the list to insert the node in the proper position
    def sorted_insert(self, value):
        temp = self.Node(value)
        curr = self.head
        self.count += 1
        if curr == None:
            self.head = temp
            self.tail = temp
        if self.head.value <= value:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp
        while curr.next != None and curr.next.value > value:
            curr = curr.next
        if curr.next == None:
            self.tail = temp
            temp.prev = curr
            curr.next = temp
        else:
            temp.next = curr.next
            temp.prev = curr
            curr.next = temp
            temp.next.prev = temp

    # remove_duplicates removes duplicate values from the sorted list
    def remove_duplicates(self):
        curr = self.head
        delete = self.Node()
        while curr != None:
            if curr.next != None and curr.value == curr.next.value:
                delete = curr.next
                curr.next = delete.next
                curr.next.prev = curr
                if delete == self.tail:
                    self.tail = curr
            else:
                curr = curr.next

    # reverse reverses the list iterativley
    def reverse(self):
        curr = self.head
        temp = self.Node()
        while curr != None:
            temp = curr.next
            curr.next = curr.prev
            curr.prev = temp
            if curr.prev == None:
                self.tail = self.head
                self.head = curr
                return
            curr = curr.prev
        return

    # copy_list_reversed copies the list reversed to a new list
    def copy_list_reversed(self):
        dll = DoublyLinkedList()
        curr = self.head
        while curr != None:
            dll.add_head(curr.value)
            curr = curr.next
        return dll

    # copy_list copies the list to a new list
    def copy_list(self):
        dll = DoublyLinkedList()
        curr = self.head
        while curr != None:
            dll.add_tail(curr.value)
            curr = curr.next
        return dll