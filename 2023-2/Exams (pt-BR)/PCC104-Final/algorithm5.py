def is_upper_triangular(matrix[0,...,n-1][0,...,n-1]):

    for i in range(0,n):
        for j in range(i,n):
            if matrix[i][j] != 0:
                return False
    return True
