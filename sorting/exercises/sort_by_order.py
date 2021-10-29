# Sort First Array by Order In Second Array

# Worst Case:           O(n)
# Average Case:         O(n)

def sort_by_order(arr1, arr2):
    mp = {}
    size = len(arr1)
    arr = [0] * size
    j = 0
    for i in range(size):
        if arr1[i] in mp:
            mp[arr1[i]] += 1
        else:
            mp[arr1[i]] = 1
    for key in arr2:
        if key in mp:
            for i in range(mp[key]):
                arr[j] = key
                j += 1
            del(mp[key])
    for key in mp:
        for i in range(mp[key]):
            arr[j] = key
            j += 1
    return arr

def main():
    array1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
    array2 = [2, 1, 8, 3]
    print(array1)
    print(array2)
    array1 = sort_by_order(array1, array2)
    print(array1)

if __name__ == "__main__":
    main()