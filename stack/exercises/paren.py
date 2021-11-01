# Push element at the bottom of the stack

# Time Complexity:  O(n)

import math

def is_balanced(expn):
    stk = []
    for ch in expn:
        if ch in ['{', '[', '(']:
            stk.append(ch)
        elif ch == '}':
            if stk.pop() != '{':
                return False
        elif ch == ']':
            if stk.pop() != '[':
                return False
        elif ch == ')':
            if stk.pop() != '(':
                return False
    return True

def max_depth(expn):
    stk = []
    max_depth = 0
    depth = 0
    for ch in expn:
        if ch == "(":
            stk.append(ch)
            depth += 1
        elif ch == ')':
            stk.pop()
            depth -= 1
        if depth > max_depth:
            max_depth = depth
    return max_depth

def max_depth_nostack(expn):
    max_depth = 0
    depth = 0
    for ch in expn:
        if ch == "(":
            depth += 1
        elif ch == ')':
            depth -= 1
        if depth > max_depth:
            max_depth = depth
    return max_depth

def cont_balanced_paren(string):
    size = len(string)
    stk = []
    stk.append(-1)
    length = 0
    for i in range(size):
        if string[i] == '(':
            stk.append(i)
        elif string[i] == ')':
            stk.pop()
            if len(stk) == 0:
                stk.append(i)
            else:
                length = max(length, 1 - stk[-1])
    return length

def reverse_paren(expn):
    stk = []
    if len(expn) % 2 == 1:
        return -1
    open_count = 0
    close_count = 0
    for ch in expn:
        if ch == '(':
            stk.append(ch)
        elif ch == ')':
            if len(stk) != 0 and stk[-1] == '(':
                stk.pop()
            else:
                stk.append(')')
    while len(stk) != 0:
        if stk.pop() == '(':
            open_count += 1
        else:
            close_count += 1
    reversal = math.ceil(open_count // 2) + math.ceil(close_count // 2)
    return reversal

def find_dup_paren(expn):
    stk = []
    for ch in expn:
        if ch == ')':
            count = 0
            while len(stk) != 0 and stk[-1] != '(':
                stk.pop()
                count += 1
            if count <= 1:
                return True
        else:
            stk.append(ch)
    return False

def print_paren_num(expn):
    stk = []
    output = []
    count = 1
    for ch in expn:
        if ch == '(':
            stk.append(count)
            output.append(count)
            count += 1
        elif ch == ')':
            output.append(stk.pop())
    print(output)