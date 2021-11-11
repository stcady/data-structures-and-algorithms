# Find the largest path that contains the largest number of 1s (land)

def find_largest_island_util(arr, max_col, max_row, curr_col, curr_row, value, traversed):
    if curr_col < 0 or curr_col >= max_col or curr_row < 0 or curr_row >= max_row:
        return 0
    if traversed[curr_col][curr_row] == 1 or arr[curr_col][curr_row] != value:
        return 0
    traversed[curr_col][curr_row] = 1
    # each call corresponds to 8 directions
    return 1 + find_largest_island_util(arr, max_col, max_row, curr_col - 1, curr_row - 1, value, traversed) + find_largest_island_util(arr, max_col, max_row, curr_col - 1, curr_row, value, traversed) + find_largest_island_util(arr, max_col, max_row, curr_col - 1, curr_row + 1, value, traversed) + find_largest_island_util(arr, max_col, max_row, curr_col, curr_row - 1, value, traversed) + find_largest_island_util(arr, max_col, max_row, curr_col, curr_row + 1, value, traversed) + find_largest_island_util(arr, max_col, max_row, curr_col + 1, curr_row - 1, value, traversed) + find_largest_island_util(arr, max_col, max_row, curr_col + 1, curr_row, value, traversed) + find_largest_island_util(arr, max_col, max_row, curr_col + 1, curr_row + 1, value, traversed)

infi = 99999
def find_largest_island(arr, max_col, max_row):
    max_val = 0
    curr_val = 0
    traversed = [[infi] * max_col for _ in range(max_row)]
    for i in range(max_col):
        for j in range(max_row):
            curr_val = find_largest_island_util(arr, max_col, max_row, i, j, arr[i][j], traversed)
            if curr_val > max_val:
                max_val = curr_val
    return max_val

def main():
    arr = [[1, 0, 1, 1, 0], [1, 0, 0, 1, 0], [0, 1, 1, 1, 1], [0, 1, 0, 0, 0], [1, 1, 0, 0, 1]]
    print("Largest Island: ", find_largest_island(arr, 5, 5))

if __name__ == "__main__":
    main()