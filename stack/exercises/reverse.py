# Push element at the bottom of the stack

# Time Complexity:  O(n^2)

import linkedlist_stack as lls
import bottom_insert as bi

def reverse(stk: lls.Stack):
    if stk.is_empty() == False:
        temp = stk.pop()
        reverse(stk)
        bi.bottom_insert(stk, temp)

def main():
    s = lls.Stack()
    s.push(1)
    s.push(9)
    s.push(2)
    reverse(s)
    s.print_stack()

if __name__ == "__main__":
    main()