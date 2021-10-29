# Push element in sorted order

# Time Complexity:  O(n^2)

import linkedlist_stack as lls
import insert_sorted as insort

def sort_stack_recurse(stk: lls.Stack):
    if stk.is_empty() == False:
        temp = stk.pop()
        sort_stack_recurse(stk)
        insort.sorted_insert(stk, temp)

def sort_stack(stk: lls.Stack):
    stk2 = lls.Stack()
    while stk.is_empty() == False:
        temp = stk.pop()
        while stk2.is_empty() == False and stk2.peek() < temp:
            stk.push(stk2.pop())
        stk2.push(temp)
    while stk2.is_empty() == False:
        stk.push(stk2.pop())

def main():
    s = lls.Stack()
    s.push(1)
    s.push(9)
    s.push(2)
    sort_stack_recurse(s)
    s.print_stack()

if __name__ == "__main__":
    main()