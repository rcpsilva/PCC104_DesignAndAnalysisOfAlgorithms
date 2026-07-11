from math import inf
from heapq import heappush, heappop

def print_L(c,L):
    print(f'{c}: ')
    for v in L:
        print(v)
    

def dijkistra(G,w,s):
    V = [{'id':i,'pai':None, 'd':inf} for i in range(len(G))]
    V[s]['d'] = 0

    F = []
    Q = []

    for vi in V:
        heappush(Q,(vi['d'],vi['id']))

    while Q:
        _ , u = heappop(Q)
        if u not in F:
            u = V[u]
            F.append(u['id'])
            for vi in G[u['id']]:
                if vi not in F:
                    v = V[vi]
                    cd = (u['d'] + w[(u['id'],v['id'])])
                    if v['d'] > cd:
                        v['d'] = cd
                        v['pai'] = u['id']
                        heappush(Q,(v['d'],v['id']))

            print(f'Q: \n {Q}')
            print_L('V',V)
            print_L('F',F)        
    
    return F



if __name__ == '__main__':

    G = {0: [1,2],
         1: [2,3],
         2: [1,3,4],
         3: [4],
         4: [3,0]}
    
    pesos_arestas = {
        (0,1): 10,
        (0,2): 5,
        (1,2): 2,
        (1,3): 1,
        (2,1): 3,
        (2,3): 9,
        (2,4): 2,
        (3,4): 4,
        (4,3): 6,
        (4,0): 7
    }

    dijkistra(G,pesos_arestas,0)