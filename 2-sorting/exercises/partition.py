# Array Partitioning
#   Partition array of 0s and 1s
#   Partition array of 0s, 1s, and 2s
#   Partition array based on provided range value

# Worst Case:           O(n)
# Average Case:         O(n)

def partition01(arr):
    size = len(arr)
    left = 0
    right = size - 1
    while left < right:
        while arr[left] == 0:
            left += 1
        while arr[right] == 1:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]

def partition012(arr):
    size = len(arr)
    left = 0
    right = size - 1
    i = 0
    while i <= right:
        if arr[i] == 0:
            arr[i], arr[left] = arr[left], arr[i]
            i += 1
            left += 1
        elif arr[i] == 2:
            arr[i], arr[right] = arr[right], arr[i]
            right -= 1
        else:
            i += 1

def range_partition(arr, lower, higher):
    size = len(arr)
    left = 0
    right = size - 1
    i = 0
    while i <= right:
        print(arr, i)
        if arr[i] < lower:
            arr[i], arr[left] = arr[left], arr[i]
            i += 1
            left += 1
        elif arr[i] > right:
            arr[i], arr[right] = arr[right], arr[i]
            right -= 1
        else:
            i += 1


def main():
    array = [0, 1, 0, 1, 1, 1]
    print(array)
    partition01(array)
    print(array)
    array = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    print(array)
    partition012(array)
    print(array)
    array = [1, 21, 2, 20, 3, 19, 4, 18, 5, 17, 6, 16, 7, 15, 8, 14, 9, 13, 10, 12, 11]
    range_partition(array, 8, 12)

if __name__ == "__main__":
    main()