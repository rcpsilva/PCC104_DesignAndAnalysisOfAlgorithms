def find_max(matrix, row=0, col=0, max_val=None):

    n = len(matrix)
    m = len(matrix[0])

    if row == n:
        return max_val

    if matrix[row][col] > max_val:
        max_val = matrix[row][col]

    if col == m - 1:
        return find_max(matrix, row + 1, 0, max_val)
    else:
        return find_max(matrix, row, col + 1, max_val)