# Selection Sort Algorithm

# Worst Case:           O(n^2)
# Average Case:         O(n^2)
# Best Case:            O(n^2)
# Space Complexity:     O(1)

def max_selection_sort(arr):
    size = len(arr)
    # iterate through array
    for i in range(size - 1):
        maxIndex = 0
        # find largest value in remaining array
        for j in range(1, size - 1 - i):
            if arr[j] > arr[maxIndex]:
                maxIndex = j
        # swap ith last element with largest element
        temp = arr[size - 1 - i]
        arr[size - 1 - i] = arr[maxIndex]
        arr[maxIndex] = temp
        print(arr)

def min_selection_sort(arr):
    size = len(arr)
    # iterate through array
    for i in range(size - 1):
        minIndex = 1
        # find smallest value in remaining array
        for j in range(i + 1, size):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # swap ith element with smallest element
        temp = arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex] = temp
        print(arr)

def more(value1, value2):
    return value1 > value2

def main():
    print("Max Order...")
    array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    print(array)
    max_selection_sort(array)
    print("Min Order...")
    array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    print(array)
    min_selection_sort(array)

if __name__ == "__main__":
    main()