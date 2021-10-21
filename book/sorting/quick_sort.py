# Quick Sort Algorithm

# Worst Case:           O(n^2)
# Average Case:         O(nlogn)
# Best Case:            O(nlogn)
# Space Complexity:     O(nlongn)

def QuickSort(arr):
    size = len(arr)
    tempArray = [0] * size
    quickSortUtil(arr, 0, size - 1)

def quickSortUtil(arr, lower, upper):
    print(arr)
    #terminating condition
    if upper <= lower:
        return
    # set pivot and start/stop indices
    pivot = arr[lower]
    start = lower
    stop = upper
    # iterate while lower pointer is less than upper pointer
    while lower < upper:
        # increment until value >= pivot is found
        while arr[lower] <= pivot and lower < upper:
            lower += 1
        # decrement until value < pivot is found
        while arr[upper] > pivot and lower <= upper:
            upper -= 1
        # swap upper element with lower element
        if lower < upper:
            swap(arr, upper, lower)
    # swap upper element with starting element
    swap(arr, upper, start)
    # recursivley partition on lower half
    quickSortUtil(arr, start, upper - 1)
    # recursivley partition on upper half
    quickSortUtil(arr, upper + 1, stop)

def swap(arr, first, second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp    

def main():
    array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    QuickSort(array)

if __name__ == "__main__":
    main()