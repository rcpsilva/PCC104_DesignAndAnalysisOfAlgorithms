# 'Busca em largura' para gerar todas as combinações
def dfs_M(M):
    
    directions = [(1,0),(-1,0),(0,-1),(0,1)]

    inicio = None
    fim = None
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 1:
                inicio = (i,j)
            if M[i][j] == 2:
                fim = (i,j)


    L = [[inicio]]
    visited = set()

    while L:   
        print(L)
        s = L.pop(-1)
        visited.add(s[-1])

        if fim == s[-1]:
            return True
        else:
            domain = [(s[-1][0] + d[0], s[-1][1] + d[1]) for d in directions]
            for e in domain:
                if e not in visited:
                    if e[0]>=0 and e[0]<len(M) and e[1]>=0 and e[1]<len(M[0]):
                        if M[e[0]][e[1]] > 0:
                            L.append(s + [e])

    return False

if __name__ == '__main__':

    M1 = [[3,0,3,0,0],
        [3,0,0,0,3],
        [3,3,3,3,3],
        [0,2,3,0,0],
        [3,0,0,1,3]]

    M2 = [[3,0,3,0,0],
          [3,0,0,0,3],
          [3,3,3,3,3],
          [0,2,3,3,0],
          [3,0,0,1,3]]
    
    print(dfs_M(M2))