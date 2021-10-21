# Insertion Sort Algorithm

# Worst Case:           O(n^2)
# Average Case:         O(n^2)
# Best Case:            O(n)
# Space Complexity:     O(1)

def InsertionSort(arr):
    size = len(arr)
    i = 1
    # iterate through array
    while i < size:
        temp = arr[i]
        j = i
        # shift array right while previous elements is larger than current
        while j > 0 and more(arr[j - 1], temp):
            arr[j] = arr[j - 1]
            j -= 1
            print(arr)
        # insert element
        arr[j] = temp
        i += 1
        print(arr)


def more(value1, value2):
    return value1 > value2

def main():
    array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    print(array)
    InsertionSort(array)

if __name__ == "__main__":
    main()