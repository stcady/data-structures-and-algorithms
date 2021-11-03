from singly_linked_list import LinkedList

def main():
    l = LinkedList()
    l.add_head(9)
    l.add_head(6)
    l.add_head(4)
    l.print_list()
    print()
    l.reverse_recurse()
    print()
    l.print_list()

if __name__ == "__main__":
    main()