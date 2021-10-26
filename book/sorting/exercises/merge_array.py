# Merge Two Sorted Arrays
# does not consider second array being longer than the first array

# Worst Case:           O(m*n)
# Average Case:         O(m*n)

def merge(arr1, arr2):
    size1 = len(arr1)
    size2 = len(arr2)
    first = 0
    while first < size1:
        if arr1[first] <= arr2[0]:
            first += 1
        else:
            arr1[first], arr2[0] = arr2[0], arr1[first]
            first += 1
            for i in range(size2 - 1):
                if arr2[i] < arr2[i + 1]:
                    break
                arr2[i], arr2[i + 1] = arr2[i + 1], arr2[i]

def main():
    array1 = [1, 5, 9, 10, 15, 20]
    array2 = [2, 3, 8, 13]
    print(array1, array2)
    merge(array1, array2)
    print(array1, array2)

if __name__ == "__main__":
    main()