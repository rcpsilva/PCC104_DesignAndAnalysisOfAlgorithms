from bt_visualizations import draw_chessboard

def viable(sol, i, v):

    if v in sol:
        return False
    
    for j in range(0,i):
        delta_row = abs(i-j)
        delta_col = abs(sol[j] - v)

        if delta_col == delta_row:
            return False
        
    return True

def backtracking(n):
    return bt([-1 for i in range(n)])

def bt(sol):

    if sol[-1] != -1:
        return sol
    else:
        for i in range(len(sol)):
            if sol[i] == -1:
                for v in range(len(sol)):
                    if viable(sol,i,v):
                        sol[i] = v 
                        sol = bt(sol)  
                        
                        if sol[-1] != -1:
                            return sol
                        sol[i] = -1

                return sol

if __name__ == '__main__':

    sol = backtracking(10)

    print(sol)

    draw_chessboard(sol)







    
