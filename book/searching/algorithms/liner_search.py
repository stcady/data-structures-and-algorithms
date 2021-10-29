# Linearly searching through array

# Time Complexity:     O(n)
# Space Complexity:    O(1) 

# unsorted_linear_search
def unsorted_linear_search(arr, size, value):
    for i in range(size):
        if value == arr[i]:
            return True
        return False

# sorted_linear_search
def sorted_linear_search(arr, size, value):
    for i in range(size):
        if value == arr[i]:
            return True
        elif value < arr[i]:
            return False
    return False