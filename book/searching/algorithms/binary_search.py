# Logarithmically searching through a sorted array

# Time Complexity:              O(logn)
# Space Complexity:             O(1)
# Recursion Space Complexity:   O(logn)

# binary_search
def binary_search(arr, size, value):
    low = 0
    high = size - 1
    while low <= high:
        mid = (low + high)/2
        if arr[mid] == value:
            return True
        elif arr[mid] < value:
            low = mid + 1
        else:
            high = mid - 1

# recursive_binary_search
def recursive_binary_search(arr, value):
    return recursive_binary_search_util(arr, 0, len(arr) - 1, value)

# recursive_binary_search_util
def recursive_binary_search_util(arr, low, high, value):
    if low > high:
        return False
    mid = (low + high)//2
    if arr[mid] == value:
        return True
    elif arr[mid] < value:
        return recursive_binary_search_util(arr, mid + 1, high, value)
    else:
        return recursive_binary_search_util(arr, low, mid - 1, value)

def main():
    first = [1, 3, 5, 7, 9, 25, 30]
    print(recursive_binary_search(first, 3))

if __name__ == "__main__":
    main()