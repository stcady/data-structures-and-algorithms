# Print the next smaller element of each element of the array

# Brute Force Time Complexity:  O(n^2)
# Time Complexity:              O(n)

import linkedlist_stack as lls

def next_smaller_bruteforce(arr):
    size = len(arr)
    output = []
    for i in range(0, size, 1):
        next = -1
        for j in range(i + 1, size, 1):
            if arr[i] > arr[j]:
                next = arr[j]
                break
        output.append(next)
    print(output)

def next_smaller(arr):
    size = len(arr)
    stk = lls.Stack()
    output = [-1]*size
    stk.push(arr[size - 1])
    i = size - 2
    while i >= 0:
        while stk.is_empty() == False:
            top = stk.peek()
            if top >= arr[i]:
                stk.pop()
            else:
                output[i] = top
                break
        if stk.is_empty():
            output[i] = -1
        stk.push(arr[i])
        i -= 1
    print(output)