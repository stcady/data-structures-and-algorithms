# Separate Even and Odd Numbers in Array

# Worst Case:           O(n)
# Average Case:         O(n)

def reduction(arr):
    size = len(arr)
    arr.sort()
    count = 1
    reduction = arr[0]
    for i in range(size):
        if arr[i] - reduction > 0:
            print(size - i)
            reduction = arr[i]
            count += 1
    print(count)

def main():
    array = [5, 1, 1, 1, 2, 3, 5]
    print(array)
    reduction(array)

if __name__ == "__main__":
    main()