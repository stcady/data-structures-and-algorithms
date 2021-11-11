# Push element in sorted order

# Time Complexity:  O(n)

import linkedlist_stack as lls

def sorted_insert(stk: lls.Stack, element):
    if stk.is_empty() or element > stk.peek():
        stk.push(element)
    else:
        temp = stk.pop()
        sorted_insert(stk, element)
        stk.push(temp)

def main():
    s = lls.Stack()
    sorted_insert(s, 1)
    sorted_insert(s, 6)
    sorted_insert(s, 3)
    s.print_stack()

if __name__ == "__main__":
    main()