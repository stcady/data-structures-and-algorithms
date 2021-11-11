# Span of stocks for each day

# Brute Force Time Complexity:  O(n^2)
# Time Complexity:              O(n)

def stock_span_range_brueforce(arr):
    SR = [0] * len(arr)
    SR[0] = 1
    i = 1
    size = len(arr)
    while i < size:
        SR[i]  = 1
        j = i - 1
        while j >= 0 and arr[i] >= arr[j]:
            SR[i] += 1
            j -= 1
        i += 1
    return SR

def stock_span_range(arr):
    stk = []
    size = len(arr)
    SR = [0] * size
    stk.append(0)
    SR[0] = 1
    i = 1
    while i < size:
        while len(stk) != 0 and arr[len(stk) - 1] <= arr[i]:
            print(i, stk)
            stk.pop()
        if len(stk) == 0:
            print(i, stk)
            SR[i] = i + 1
        else:
            print(i, stk)
            SR[i] = i - stk[len(stk) - 1]
        stk.append(i)
        i += 1
    return SR

def main():
    arr = [5, 4, 3, 2, 1, 3, 4, 5, 6]
    sr = stock_span_range(arr)
    print(sr)

if __name__ == "__main__":
    main()