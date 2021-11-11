# Sort By Power Equation from Given Exponent Value

# Worst Case:           O(n^2)
# Average Case:         O(n^2)

def equation_sort(arr, A):
    size = len(arr)
    for i in range(size - 1):
        for j in range(size - i - 1):
            if more(arr[j], arr[j + 1], A):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
def more(value1, value2, A):
    return pow(value1, A) > pow(value2, A)

def main():
    array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    print(array)
    equation_sort(array, 5)
    print(array)

if __name__ == "__main__":
    main()