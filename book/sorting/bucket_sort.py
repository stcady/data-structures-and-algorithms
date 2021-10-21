# Bucket Sort Algorithm

# Worst Case:           O(n+k)
# Average Case:         O(n+k)
# Space Complexity:     O(k)

def BucketSort(arr, lowerRange, upperRange):
    size = len(arr)
    # set range
    dataRange = upperRange - lowerRange
    count = [0] * size
    # count array
    for i in range(size):
        count[arr[i] - lowerRange] += 1
    j = 0
    # generate sorted output by iterativley inserting count values
    for i in range(dataRange):
        while count[i] > 0:
            arr[j] = i + lowerRange
            count[i] -= 1
            j += 1
    print(arr)

def main():
    array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    print(array)
    BucketSort(array, 1, 10)

if __name__ == "__main__":
    main()