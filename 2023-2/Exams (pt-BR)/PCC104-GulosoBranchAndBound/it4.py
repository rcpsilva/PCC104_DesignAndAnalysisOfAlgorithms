def algorithm(matrix):

    n = len(matrix)  

    for row in matrix:
        if len(row) != n:
            return False
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False

    return True


