# Push element at the bottom of the stack

# Time Complexity:  O(n^2)

import dequeue_queue as dq

def reverse(que: dq.Queue):
    if que.is_empty() == False:
        stk = []
        while not que.is_empty():
            stk.append(que.remove())
        while len(stk) != 0:
            que.add(stk.pop())
    return que

def main():
    que = dq.Queue()
    i = 0
    while i < 20:
        que.add(i)
        i += 1
    que.print_queue()
    reverse(que).print_queue()

if __name__ == "__main__":
    main()