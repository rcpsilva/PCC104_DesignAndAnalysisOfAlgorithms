import numpy as np
from copy import copy
import heapq as hq

def cost(C,sol):

    cost = 0
    for i,s in enumerate(sol):
        cost += C[i][s]

    return cost 

def h(C,sol):

    val = 0
    for i in range(len(sol),len(C)):
        val += np.min(C[i])

    return val


def is_possible(sol,v):

    return v not in sol

def bestfirst_bb(C):

    F = []
    best = []
    best_cost = np.infty

    for i in range(len(C)):
        hq.heappush(F,(cost(C,[i]) + h(C,[i]),[i]))

    while F:
        sol = hq.heappop(F)
        f = sol[0]
        sol = sol[1]
        
        if len(sol) == len(C):
            best_cost = f
            best = sol
        else:
            for v in range(len(C[0])):
                if is_possible(sol,v):
                    f = cost(C,sol+[v]) + h(C,sol+[v])    
                    if f < best_cost:
                        hq.heappush(F,(f,sol+[v]))

    return best, best_cost

def bb(C, best, best_cost, sol=[]):

    if len(sol) == len(C):
        print(sol)
        if cost(C,sol) < best_cost:
            best_cost = cost(C,sol)
            best = copy(sol)
    else:
        for v in range(len(C[0])):
            if is_possible(sol,v) and ((cost(C,sol+[v]) + h(C,sol+[v])) < best_cost):
               best, best_cost = bb(C, best, best_cost, sol + [v])
        
    return best, best_cost

def bex(C, best, best_cost, sol=[]):

    if len(sol) == len(C):
        print(sol)
        if cost(C,sol) < best_cost:
            best_cost = cost(C,sol)
            best = copy(sol)
    else:
        for v in range(len(C[0])):
            if is_possible(sol,v):
               best, best_cost = bex(C, best, best_cost, sol + [v])
        
    return best, best_cost

if __name__ == '__main__':
        # t0,t1,t2,t3
    C = [[9,2,7,8], # pessoa 0
         [6,4,3,7], # pessoa 1
         [5,8,1,8], # pessoa 2
         [4,6,9,4]] # pessoa 3
    
    best = []
    best_cost = np.infty

    #best, best_cost = bex(C, best, best_cost)
    #best, best_cost = bb(C, best, best_cost)
    
    best, best_cost = bestfirst_bb(C)

    print(f'Solution: {best} Cost: {best_cost}')