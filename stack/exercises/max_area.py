# Find the maximum area rectangle in a histogram

# Brute Force Time Complexity:  O(n^2)
# Time Complexity:              O(n)

def max_area_bruteforce(arr):
    size = len(arr)
    max_area = -1
    min_height = 0
    i = 1
    while i < size:
        min_height = arr[i]
        j = j - 1
        while j >= 0:
            if min_height > arr[j]:
                min_height = arr[j]
            curr_area = min_height * (i - j + 1)
            if max_area < curr_area:
                max_area = curr_area
            j -= 1
        i += 1
    return max_area

def max_area(arr):
    size = len(arr)
    stk = []
    max_area = 0
    i = 0
    while i < size:
        while len(stk) != 0 and arr[stk[len(stk) - 1]] <= arr[i]:
            stk.append(i)
        while not len(stk) == 0 and (i == size or arr[stk[len(stk) - 1]] > arr[i]):
            top = stk[len(stk) - 1]
            stk.pop()
            top_area = arr[top] * (i if len(stk) == 0 else i - stk[len(stk) - 1] - 1)
            if max_area < top_area:
                max_area = top_area
    return max_area
