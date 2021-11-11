from collections import deque

def max_sliding_windows(arr, k):
    size = len(arr)
    que = deque([])
    for i in range(size):
        # remove out of range elements
        if que and que[0] <= i - k:
            que.popleft()
        # remove smaller values at left
        while que and arr[que[-1]] <= arr[i]:
            que.pop()
        que.append(i)
        # window of size k
        if i >= (k - 1):
            print(arr[que[0]])

def min_of_max_sliding_windows(arr, k):
    size = len(arr)
    que = deque()
    min_val = 999999
    for i in range(size):
        # remove out of range elements
        if que and que[0] <= i - k:
            que.popleft()
        # remove smaller values at left
        while que and arr[que[-1]] <= arr[i]:
            que.pop()
        que.append(i)
        # window of size k
        if i >= (k - 1) and min_val > arr[que[0]]:
            min_val = arr[que[0]]
    print("Min of max is : ", min_val)

def max_of_min_sliding_windows(arr, k):
    size = len(arr)
    que = deque()
    max_val = -999999
    for i in range(size):
        # remove out of range elements
        if que and que[0] <= i - k:
            que.popleft()
        # remove smaller values at left
        while que and arr[que[-1]] <= arr[i]:
            que.pop()
        que.append(i)
        # window of size k
        if i >= (k - 1) and max_val < arr[que[0]]:
            max_val = arr[que[0]]
    print("Max of min is : ", max_val)

def first_neg_sliding_windows(arr, k):
    size = len(arr)
    que = deque()
    for i in range(size):
         # remove out of range elements
        if que and que[0] <= i - k:
            que.popleft()
        if arr[i] < 0:
            que.append(i)
        if i >= (k - 1):
            if len(que) > 0:
                print(arr[que[0]])
            else:
                print("NaN")

def main():
    print("max_sliding_windows")
    max_sliding_windows([11, 2, 75, 92, 59, 90, 55], 3)
    print("min_of_max_sliding_windows")
    min_of_max_sliding_windows([11, 2, 75, 92, 59, 90, 55], 3)
    print("max_of_min_sliding_windows")
    max_of_min_sliding_windows([11, 2, 75, 92, 59, 90, 55], 3)
    print("first_neg_sliding_windows")
    first_neg_sliding_windows([13, -2, -6, 10, -14, 50, 14, 21], 3)


if __name__ == "__main__":
    main()