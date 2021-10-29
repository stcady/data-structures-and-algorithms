# Minimum Swapping

# Worst Case:           O(n)
# Average Case:         O(n)

def min_swaps(arr):
    size = len(arr)
    start = 0
    end = size - 1
    count = 0
    while start < end:
        if arr[start] == 0:
            start += 1
        elif arr[end] == 1:
            end -= 1
        else:
            arr[start], arr[end] = arr[end], arr[start]
            count += 1
        print(arr, count)
    
def main():
    array = [0, 1, 0, 1, 0]
    min_swaps(array)

if __name__ == "__main__":
    main()