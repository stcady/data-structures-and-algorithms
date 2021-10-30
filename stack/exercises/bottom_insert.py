# Push element at the bottom of the stack

# Time Complexity:  O(n)

import linkedlist_stack as lls
import insert_sorted as insort

def bottom_insert(stk: lls.Stack, element):
    if stk.is_empty():
        stk.push(element)
    else:
        temp = stk.pop()
        bottom_insert(stk, element)
        stk.push(temp)

def main():
    s = lls.Stack()
    s.push(1)
    s.push(9)
    s.push(2)
    bottom_insert(s, 7)
    s.print_stack()

if __name__ == "__main__":
    main()