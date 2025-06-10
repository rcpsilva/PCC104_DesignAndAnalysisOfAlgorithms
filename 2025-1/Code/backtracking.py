'''procedure BACKTRACK(solucao_parcial):
    se solucao_parcial é uma solução completa então
        processa(solucao_parcial)  # exibe, armazena ou conta a solução
        retorne
    fim-se

    para cada escolha possível e válida a partir de solucao_parcial faça:
        faça a escolha (adicione ao estado atual)
        BACKTRACK(nova solucao_parcial)
        desfaça a escolha (retorne ao estado anterior)
    fim-para
end procedure '''

import math
def is_valid_perm(s,v):

    if v in s:
        return False

    return True

def cost(sol,G):
    cost = 0

    for i in range(len(sol)):
        cost += G[sol[i]][sol[(i+1)%len(sol)]]
    
    return cost

def bk_perm(n,G,sol,min_cost,best_sol):
    if len(sol)==n:
        c = cost(sol,G)
        if c < min_cost:
            min_cost = c
            best_sol = sol
            print(f'cost: {c} sol: {best_sol}')
        return min_cost, best_sol
    else:
        for i in range(n):
            if is_valid_perm(sol,i):
                sol.append(i)
                min_cost, best_sol = bk_perm(n,G,sol,min_cost,best_sol)
                sol.pop()

        return min_cost, best_sol

def is_valid_choice(sol,v):

    if v in sol:
        return False

    linha = len(sol)

    for i in range(len(sol)):
        if abs(i-linha) == abs(sol[i]-v):
            return False
        
    return True

def backtracking(sol=[],n=8):

    print(sol)
    if len(sol)==n:
        print(sol)
    else:
        for choice in range(n):
            if is_valid_choice(sol,choice):
                sol.append(choice)
                backtracking(sol,n)
                sol.pop(-1)

if __name__ == '__main__':

    # backtracking([],4)

    G = [[0,8,9,1,1,5,1,4,5],
         [4,0,2,3,4,7,8,9,9],
         [5,1,0,3,4,1,2,3,4],
         [2,1,2,0,4,8,7,6,5],
         [2,1,2,0,4,7,3,1,2],
         [2,1,2,0,4,23,5,1,2],
         [2,1,2,0,4,13,2,1,4],
         [2,1,2,0,4,5,6,7,8],
         [1,1,2,3,0,1,1,4,4]]
    
    min_cost = math.inf
    best_sol = None
    min_cost, best_sol = bk_perm(len(G),G,sol=[0],min_cost=min_cost,best_sol=best_sol)
    print(f'min_cost: {min_cost} sol: {best_sol}')
