def search(s,G,O,V,type='dfs'):

    V[s] = [s,'C',None,0]

    F = [V[s]]

    while F:
        print(F)
       
        if type == 'dfs':
            x = F.pop(-1)
        elif type == 'bfs':
            x = F.pop(0)
        else:
            ValueError(f'Invalid search type {type}')

        if x[0] in O:
            return x 

        for xi in G[x[0]]:
            if V[xi][1] == 'B':
                V[xi][1] = 'C' 
                V[xi][2] = x[0]
                V[xi][3] = V[x[0]][3] + 1
                F.append(V[xi])

        V[x[0]][1] = 'P'

    return None   

def get_path(v, V):
    path = [v[0]]

    while v[2]:
        path.append(v[2])
        v = V[v[2]]

    path.append(v[2])
    path.reverse()

    return path 
if __name__ == '__main__':

    G = [[1,2,3],
         [6,4,0],
         [0,5,7],
         [0,4,5],
         [1,3],
         [2,3],
         [1,8],
         [2,8],
         [6,7]]
    
    V = [[i,'B',None,-1] for i in range(len(G))]
    s = 0
    O = [7,8]

    obj = search(s,G,O,V,'bfs')

    print(f'Objetivo: {obj}')

    path = get_path(obj,V)

    print(f'Path: {path}')
