# Find the minimum number of steps required to move a knight from start position to final position

def steps_of_knight_util(size, curr_col, curr_row, traversed, dist):
    # range check
    if curr_col < 0 or curr_col >= size or curr_row < 0 or curr_row >= size:
        return
    # traversable
    if traversed[curr_col][curr_row] <= dist:
        return
    # update
    traversed[curr_col][curr_row] = dist
    steps_of_knight_util(size, curr_col - 2, curr_row - 1, traversed, dist + 1)
    steps_of_knight_util(size, curr_col - 2, curr_row + 1, traversed, dist + 1)
    steps_of_knight_util(size, curr_col + 2, curr_row - 1, traversed, dist + 1)
    steps_of_knight_util(size, curr_col + 2, curr_row + 1, traversed, dist + 1)
    steps_of_knight_util(size, curr_col - 1, curr_row - 2, traversed, dist + 1)
    steps_of_knight_util(size, curr_col + 1, curr_row - 2, traversed, dist + 1)
    steps_of_knight_util(size, curr_col - 1, curr_row + 2, traversed, dist + 1)
    steps_of_knight_util(size, curr_col + 1, curr_row + 2, traversed, dist + 1)

    infi = 99999
    def steps_of_knight(size, src_x, src_y, dist_x, dist_y):
        traversed = [[infi] * size for _ in range(size)]
        steps_of_knight_util(size, src_x - 1, src_y - 1, traversed, 0)
        for i in range(size):
            print(traversed[i])
        return traversed[dist_x - 1][dist_y - 1]
