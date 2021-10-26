# Sort Arrays and Generate Union and Intersection Lists

# Worst Case:           O(nlogn)
# Average Case:         O(nlogn)

def union_intersection_sorted(arr1, arr2):
    size1 = len(arr1)
    size2 = len(arr2)
    first, second = 0, 0
    union = []
    inter = []
    while first < size1 and second < size2:
        if arr1[first] == arr2[second]:
            union.append(arr1[first])
            inter.append(arr1[first])
            first += 1
            second += 1
        elif arr1[first] < arr2[second]:
            union.append(arr1[first])
            first += 1
        else:
            union.append(arr2[second])
            second += 1
    
    while first < size1:
        union.append(arr1[first])
        first += 1
    while second < size2:
        union.append(arr2[second])
        second += 1
    print(union, inter)
    
def union_intersection_unsorted(arr1, arr2):
    arr1.sort()
    arr2.sort()
    union_intersection_sorted(arr1, arr2)
        

def main():
    array1 = [1, 11, 2, 3, 14, 5, 6, 8, 9]
    array2 = [2, 4, 5, 12, 7, 8, 13, 10]
    print(array1, array2)
    union_intersection_unsorted(array1, array2)
    print(array1, array2)

if __name__ == "__main__":
    main()