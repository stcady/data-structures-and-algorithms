# Find If Reversing a Sub-Array Makes the Array Sorted

# Worst Case:           O(n)
# Average Case:         O(n)

def check_reverse(arr):
    size = len(arr)
    start = -1
    stop = -1
    for i in range(size - 1):
        if arr[i] > arr[i + 1]:
            start = i
            break
    if start == -1:
        return True
    for i in range(start, size - 1):
        if arr[i] < arr[i + 1]:
            stop = i
            break
    if stop == -1:
        return True
    if arr[start - 1] > arr[stop] or arr[stop + 1] < arr[start]:
        return False
    for i in range(stop + 1, size - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
        

def main():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(check_reverse(array))

if __name__ == "__main__":
    main()