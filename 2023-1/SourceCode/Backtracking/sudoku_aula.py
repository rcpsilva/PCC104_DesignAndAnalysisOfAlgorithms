from bt_visualizations import draw_sudoku, draw_sudoku_txt
from math import floor

def viable(sol, v, i, j):

    if v in sol[i]:
        return False
    
    for ii in range(len(sol)):
        if sol[ii][j] == v:
            return False
    
    bloco_linha = floor(i/3)
    bloco_coluna = floor(j/3)

    for ii in range(bloco_linha*3, bloco_linha*3+3):
        for jj in range(bloco_coluna*3, bloco_coluna*3+3):
            if v == sol[ii][jj]:
                return False
            
    return True

def complete2(sol, i, j):
    return (i == (len(sol)-1)) and (j == (len(sol)-1))

def complete(sol):
    
    for i in range(len(sol)):
        if 0 in sol[i]:
            return False
    
    return True

def backtracking(sol, viable, complete, dom):
    # Verifica se solução completa
    if complete(sol):
        return sol
    else:
        for i in range(len(sol)):
            for j in range(len(sol)):
                if sol[i][j] == 0:
                    for v in dom:
                        if viable(sol, v, i, j):
                            sol[i][j] = v
                            sol = backtracking(sol, viable, complete, dom)
                            if complete(sol):
                                return sol
                            sol[i][j] = 0
                    return sol

def backtracking2(sol, viable, complete, dom):

    for i in range(len(sol)):
        for j in range(len(sol)):
            if sol[i][j] == 0:
                for v in dom:
                    if viable(sol, v, i, j):
                        sol[i][j] = v
                        sol = backtracking2(sol, viable, complete, dom)
                        if complete(sol):
                            return sol
                        sol[i][j] = 0
                return sol
            
            if complete2(sol,i,j):
                return sol

if __name__ == '__main__':

    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 0, 0]
    ]

    #print(viable(board,0,2,1))
    
    sol = backtracking2(board, viable, complete, range(1,10))

    draw_sudoku_txt(sol)
