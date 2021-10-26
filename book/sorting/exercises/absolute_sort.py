# Sort By Absolute Value from Given Value

# Worst Case:           O(n^2)
# Average Case:         O(n^2)

def absolute_sort(arr, ref):
    size = len(arr)
    for i in range(size - 1):
        for j in range(size - i - 1):
            if more(arr[j], arr[j + 1], ref):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
def more(value1, value2, ref):
    return abs(value1 - ref) > abs(value2 - ref)

def main():
    array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    print(array)
    absolute_sort(array, 5)
    print(array)

if __name__ == "__main__":
    main()