# Find the maximum number of days in which the fruts of the whole grid will rot

infi = 99999

def rotten_fruit_util(arr, max_col, max_row, curr_col, curr_row, traversed, day):
    # range check
    if curr_col < 0 or curr_col >= max_col or curr_row < 0 or curr_row >= max_row:
        return
    # traversable and rot if not already rotten
    if traversed[curr_col][curr_row] <= day or arr[curr_col][curr_row] == 0:
        return
    # update rot time
    traversed[curr_col][curr_row] = day
    # each line corresponds to for different directions
    rotten_fruit_util(arr, max_col, max_row, curr_col - 1, curr_row, traversed, day + 1)
    rotten_fruit_util(arr, max_col, max_row, curr_col + 1, curr_row, traversed, day + 1)
    rotten_fruit_util(arr, max_col, max_row, curr_col, curr_row + 1, traversed, day + 1)
    rotten_fruit_util(arr, max_col, max_row, curr_col, curr_row - 1, traversed, day + 1)

def rotten_fruit(arr, max_col, max_row):
    traversed = [[infi] * max_col for i in range(max_row)]
    for i in range(0, max_col - 1, 1):
        for j in range(0, max_row - 1, 1):
            if arr[i][j] == 2:
                rotten_fruit_util(arr, max_col, max_row, i, j, traversed, 0)
    max_day = 0
    for i in range(0, max_col, 1):
        for j in range(0, max_row, 1):
            if arr[i][j] == 1:
                if traversed[i][j] == infi:
                    return -1
                if max_day < traversed[i][j]:
                    max_day = traversed[i][j]
    return max_day