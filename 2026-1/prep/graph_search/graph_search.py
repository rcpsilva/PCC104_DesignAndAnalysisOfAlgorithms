

def get_path(v,V):
    path = [v[0]]

    while v[2] > 0:
      path.append(v[3])
      v = V[v[3]]
    
    return path

   
def neighbors(G,v):
    return G[v[0]]

def search(G,O,s,mode='BFS'):

    V = [[i, 'B',-1,None] for i in range(len(G))]
    V[s] = [s,'C',0,None]
    Q = [V[s]]
  

    while Q:
        print(Q)

        if mode == 'BFS':
            u = Q.pop(0)
        elif mode == 'DFS':
            u = Q.pop(-1) 
        else:
           ValueError('Mode is Invalid')
        
        if u[0] in O:
            return u,V
        
        for v in neighbors(G,u):
          if V[v][1] == 'B':
            V[v][1] = 'C'
            V[v][2] = u[2] + 1
            V[v][3] = u[0] 
            Q.append(V[v])
            

        u[1] = 'P'

    return None,V



if __name__ == "__main__":

    G = [[1,2,3],
         [0,4,6],
         [0,5,6],
         [4,0,5],
         [1,3],
         [2,3],
         [1,2,8],
         [5,8],
         [7,6]]

    O = [7]
    s = 4
    r,V = search(G,O,s,'DFS')
    
    print(r)
    print(V)
    print(get_path(r,V))

