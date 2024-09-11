################# Arrays and Matrices  ################

## Indexes of subarray sum
def find_subarray(arr, n, s):
    current_sum = 0
    start = 0
    
    # Iterate over the array
    for end in range(n):
        # Add the current element to the current_sum
        current_sum += arr[end]
        
        # If the current_sum exceeds s, remove elements from the start
        while current_sum > s and start <= end:
            current_sum -= arr[start]
            start += 1
        
        # If the current_sum equals s, return the indices (1-based index)
        if current_sum == s:
            return [start + 1, end + 1]
    
    # If no subarray is found, return [-1]
    return [-1]


## Find whether path exists
# Encontrar a origem e o destino
def find_start(grid):
    n = len(grid)
    start = None
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                return [i, j]
    return start


def is_there_a_path(grid):
    n = len(grid)
    start = find_start(grid)

    flag = find_path(start[0],start[1], set(), grid, n)
    
    return 1 if flag else 0


def find_path(x, y, visited, grid, n):
    # Se chegamos ao destino
    if grid[x][y] == 2:
        return True
    
    # Marcar a célula como visitada
    visited.add((x, y))
    
    # Movimentos possíveis: cima, baixo, esquerda, direita
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Explorar cada direção
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        # Verificar se o próximo movimento é válido
        if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited and (grid[nx][ny] == 3 or grid[nx][ny] == 2):
            if find_path(nx, ny, visited, grid, n):
                return True
    
    return False



if __name__ == "__main__":
    
    # Indexes of subarray sum
    print(find_subarray([1, 2, 3, 7, 5], 5, 12))  # Output: [2, 4]
    print(find_subarray([1, 2, 7, 5], 4, 5))  # Output: [2, 4]
    print(find_subarray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 15))  # Output: [1, 5]

    
    # Whether there is a path
    grid1 = [[3, 0, 3, 0, 0], [3, 0, 0, 0, 3], [3, 3, 3, 3, 3], [0, 2, 3, 0, 0], [3, 0, 0, 1, 3]]
    grid2 = [[1, 3], [3, 2]]

    print(is_there_a_path(grid1))  # Saída esperada: 0
    print(is_there_a_path(grid2))  # Saída esperada: 1


