# Separate Even and Odd Numbers in Array

# Worst Case:           O(n)
# Average Case:         O(n)

def separate(arr):
    size = len(arr)
    left = 0
    right = size - 1
    while left < right:
        if arr[left] % 2 == 0:
            left += 1
        elif arr[right] %2 == 1:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

def main():
    array = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
    print(array)
    separate(array)
    print(array)

if __name__ == "__main__":
    main()