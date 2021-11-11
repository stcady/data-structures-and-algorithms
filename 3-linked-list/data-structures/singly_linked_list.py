class LinkedList(object):

    # Node class representing elements of linked list
    class Node:

        # Node class constructor for creating a new node
        def __init__(self, v, n=None):
            self.value = v
            self.next = n

    # LinkedList class constructur for creating a new list
    def __init__(self):
        self.head = None
        self.size = 0

    # length returns the size of the linked list
    def length(self):
        return self.size

    # find_length counts the number of nodes in the list
    def find_length(self):
        curr = self.head
        count = 0
        while curr != None:
            count += 1
            curr = curr.next
        return count

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
    
    # add_head inserts new node with the value passed at the head of the list
    def add_head(self, value):
        self.head = self.Node(value, self.head)
        self.size += 1

    # add_tail inserts new node with value passed at the end of the list
    def add_tail(self, value):
        new_node = self.Node(value, None)
        curr = self.head
        if self.head == None:
            self.head = new_node
            return
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
        self.size += 1

    # print_list prints the values in the list
    def print_list(self):
        temp = self.head
        while temp != None:
            print(temp.value, end=' ')
            temp = temp.next

    # sorted_insert iterates throught the list to insert the node in the proper position
    def sorted_insert(self, value):
        new_node = self.Node(value, None)
        curr = self.head
        if curr == None or curr.value > value:
            new_node.next = self.head
            self.head = new_node
            return
        while curr.next != None and curr.next.value < value:
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node
        self.size += 1

    # is_present searches the list to find the provided value
    def is_present(self, data):
        temp = self.head
        while temp != None:
            if temp.value == data:
                return True
            temp = temp.next
        return False

    # remove_head deletes the first node in the list
    def remove_head(self):
        if self.is_empty():
            raise RuntimeError("EmptyListException")
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value

    # delete_node deletes the first node of a provided value
    def delete_node(self, del_value):
        temp = self.head
        if self.is_empty():
            raise RuntimeError("EmptyListException")
        if del_value == self.head.value:
            self.head = self.head.next
            self.size -= 1
            return True
        while temp.next != None:
            if temp.next.value == del_value:
                temp.next = temp.next.next
                self.size -= 1
                return True
            temp = temp.next
        return False

    # delete_nodes delets all occurances of node with the specified value
    def delete_nodes(self, del_value):
        temp = self.head
        if self.is_empty():
            raise RuntimeError("EmptyListException")
        while temp != None and temp.value == del_value:
            self.head = temp.next
            temp = self.head
            self.size -= 1
        while temp != None:
            if temp.next != None and temp.next.value == del_value:
                temp.next = temp.next.next
                self.size -= 1
            else:
                temp = temp.next

    # free deletes all nodes in the list
    def free(self):
        self.head = None
        self.size = 0

    # reverse reverses the list iterativley
    def reverse(self):
        curr = self.head
        prev = None
        while curr != None:
            nextval = curr.next     # save next node
            curr.next = prev        # point current node to previous node
            prev = curr             # point the previous node to current node
            curr = nextval          # move to the next node
        self.head = prev            # point list head to last node

    # reverse_recurse reverses the list recursivley
    def reverse_recurse(self):
        self.head = self.reverse_recurse_util(self.head, None)

    # reverse_resurse_util reverses the list recursivley
    def reverse_recurse_util(self, curr_node, next_node):
        if curr_node == None:
            return None
        if curr_node.next == None:
            curr_node.next = next_node
            return curr_node
        ret = self.reverse_recurse_util(curr_node.next, curr_node)
        curr_node.next = next_node
        return ret

    # remove_duplicates removes duplicate values from the sorted list
    def remove_duplicates(self):
        curr = self.head
        while curr != None:
            if curr.next != None and curr.value == curr.next.value:
                curr.next = curr.next.next
            else:
                curr = curr.next

    # copy_list_reversed copies the list reversed to a new list
    def copy_list_reversed(self):
        temp_node = None
        curr = self.head
        while curr != None:
            temp_node2 = self.Node(curr.value, temp_node)
            curr = curr.next
            temp_node = temp_node2
        ll2 = LinkedList()
        ll2.head = temp_node
        ll2.size = self.size
        return ll2

    # copy_list copies the list to a new list
    def copy_list(self):
        curr = self.head
        if curr == None:
            return None
        tailNode = headNode = self.Node(curr.value, None)
        curr = curr.next
        while curr != None:
            temp_node = self.Node(curr.value, None)
            tailNode.next = temp_node
            tailNode = temp_node
            curr = curr.next
        ll2 = LinkedList()
        ll2.head = headNode
        ll2.size = self.size
        return ll2

    # compare_list iterates though eatch element in a list and compares
    def compare_list(self, ll2):
        head1 = self.head
        head2 = ll2.head

        while head1 != None and head2 != None:
            if head1.value != head2.value:
                return False
            head1 = head1.next
            head2 = head2.next

        if head1 == None and head2 == None:
            return True
        return False

    # compare_list_recurse iterates though eatch element in a list and compares
    def compare_list_recurse(self, ll):
        return self.compare_list_recurse_util(self.head, ll.head)

    # compare_list_recurse_util iterates though eatch element in a list and compares
    def compare_list_recurse_util(self, head1, head2):
        if head1 == None and head2 == None:
            return True
        elif (head1 == None) or (head2 == None) or (head1.value != head2.value):
            return False
        else:
            return self.compare_list_recurse_util(head1.next, head2.next)

    # nth_node_from_beginning finds the nth node from the beginning
    def nth_node_from_beginning(self, index):
        if index > self.length() or index < 1:
            raise RuntimeError("IndexOutOfRange")
        count = 1
        curr = self.head
        while curr != None and count < index:
            count += 1
            curr = curr.next
        return curr.value

    # nth_node_from_end finds the nth node from the end
    def nth_node_from_end(self, index):
        count = 1
        forward = self.head
        curr = self.head
        while forward != None and count <= index:
            count += 1
            forward = forward.next
        if forward == None:
            raise RuntimeError("IndexOutOfRange")
        while forward != None:
            forward = forward.next
            curr = curr.next
        return curr.value

    # detect_loop iterates through list to detect loop via slow and fast pointers
    def dedect_loop(self):
        slow_ptr = fast_ptr = self.head
        while fast_ptr.next != None and fast_ptr.next.next != None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                return True
        return False

    # reverse_list_detect_loop reverses the list and compares the list head to determine if loop is present
    def reverse_list_detect_loop(self):
        temp_head = self.head
        self.reverse()
        if temp_head == self.head:
            return True
        else:
            self.reverse()
            return False

    # detect_loop_type detects if loop is present delineates from circular list
    def detect_loop_type(self):
        while fast_ptr.next != None and fast_ptr.next.next != None:
            if self.head == fast_ptr.next or self.head == fast_ptr.next.next:
                return 1
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                return 1
        return 0

    # loop_point_detect returns the slow pointer node when detecting a loop
    def loop_point_detect(self):
        slowPtr = fastPtr = self.head
        while fastPtr.next != None and fastPtr.next.next != None:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
            if slowPtr == fastPtr:
                return slowPtr
        return None

    # remove_loop removes the loop in the list
    def remove_loop(self):
        loop_point = self.loop_point_detect()
        if loop_point == None:
            raise RuntimeError("LoopNotFound")
        first_ptr = self.head
        if loop_point == self.head:
            while first_ptr != self.head:
                first_ptr = first_ptr.next
            first_ptr.next = None
            return
        second_ptr = loop_point
        while first_ptr != second_ptr:
            firstPtr = firstPtr.next
            secondPtr = secondPtr.next
        secondPtr.next = None

    # find_intersection finds the intersection point of two linked lists
    def find_intersection(self, head, head2):
        l1 = 0
        l2 = 0
        temp_head = head
        temp_head2 = head2
        while temp_head != None:
            l1 += 1
            temp_head = temp_head.next
        while temp_head2 != None:
            l2 += 1
            temp_head2 = temp_head2.next
        diff = int()
        if l1 < 12:
            temp = head
            head = head2
            head2 = temp
            diff = l2 - l1
        else:
            diff = l1 - l2
        while diff > 0:
            head = head.next
            diff -= 1
        while head != head2:
            head = head.next
            head2 = head2.next
        return head


def main():
    ll = LinkedList()
    ll.add_head(1)
    ll.add_head(2)
    ll.add_head(3)
    ll.add_head(4)
    ll.print_list()

if __name__ == "__main__":
    main()
        