# Merge Sort Algorithm

# Worst Case:           O(nlogn)
# Average Case:         O(nlogn)
# Best Case:            O(nlogn)
# Space Complexity:     O(n)

def merge_sort(arr):
    size = len(arr)
    tempArray = [0] * size
    merge_sort_partition(arr, tempArray, 0, size - 1)

def merge_sort_partition(arr, tempArray, lowerIndex, upperIndex):
    #terminating condition
    if lowerIndex >= upperIndex:
        return
    # compute middle index (truncated integer)
    middleIndex = (lowerIndex + upperIndex) // 2
    # recursivley partition left and right of middle index
    merge_sort_partition(arr, tempArray, lowerIndex, middleIndex)
    merge_sort_partition(arr, tempArray, middleIndex + 1, upperIndex)
    # merge partitions
    merge(arr, tempArray, lowerIndex, middleIndex, upperIndex)

def merge(arr, tempArray, lowerIndex, middleIndex, upperIndex):
    print(arr)
    # set partition bounds
    lowerStart = lowerIndex
    lowerStop = middleIndex
    upperStart = middleIndex + 1
    upperStop = upperIndex
    # merge sort the two partitions
    count = lowerIndex
    while lowerStart <= lowerStop and upperStart <= upperStop:
        if arr[lowerStart] < arr[upperStart]:
            tempArray[count] = arr[lowerStart]
            count += 1
            lowerStart += 1
        else:
            tempArray[count] = arr[upperStart]
            count += 1
            upperStart += 1
    # fill temp array with remaining in left partition
    while lowerStart <= lowerStop:
        tempArray[count] = arr[lowerStart]
        count += 1
        lowerStart += 1
    # fill temp array with remaining in right partition
    while upperStart <= upperStop:
        tempArray[count] = arr[upperStart]
        count += 1
        upperStart += 1
    # overwrite array with sorted values
    i = lowerIndex
    while i <= upperIndex:
        arr[i] = tempArray[i]
        i += 1
    

def main():
    array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    merge_sort(array)

if __name__ == "__main__":
    main()