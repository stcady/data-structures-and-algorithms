
def dist_near_fill_util(arr, max_col, max_row, curr_col, curr_row, traversed, dist):
    # range check
    if curr_col < 0 or curr_col >= max_col or curr_row < 0 or curr_row >= max_row:
        return
    #traversable if there is a better distance
    if traversed[curr_col][curr_row] <= dist:
        return
    # update distance
    traversed[curr_col][curr_row] = dist
    dist_near_fill_util(arr, max_col, max_row, curr_col - 1, curr_row, traversed, dist + 1)
    dist_near_fill_util(arr, max_col, max_row, curr_col + 1, curr_row, traversed, dist + 1)
    dist_near_fill_util(arr, max_col, max_row, curr_col, curr_row - 1, traversed, dist + 1)
    dist_near_fill_util(arr, max_col, max_row, curr_col, curr_row + 1, traversed, dist + 1)

    infi = 99999
    def dist_near_fill(arr, max_col, max_row):
        traversed = [[infi] * max_col for _ in range(max_row)]
        for i in range(0, max_col, 1):
            for j in range(0, max_row, 1):
                if arr[i][j] == 1:
                    dist_near_fill_util(arr, max_col, max_row, i, j, traversed, 0)
        print(traversed)