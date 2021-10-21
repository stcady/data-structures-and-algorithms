# Bubble Sort Algorithm

# Worst Case:           O(n^2)
# Average Case:         O(n^2)
# Space Complexity:     O(1)

def BubbleSort(arr):
    size = len(arr)
    # iterate through array
    for i in range(size - 1):
        # shift elements left while current element is larger than next
        for j in range(size - i - 1):
            if more(arr[j], arr[j + 1]):
                # swapping
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            print(arr)

def more(value1, value2):
    return value1 > value2

def main():
    array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    print(array)
    BubbleSort(array)

if __name__ == "__main__":
    main()