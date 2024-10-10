# 'Busca em largura' para gerar todas as combinações
def dfs_M(M):
    
    # Lista de direções
    directions = [(1,0),(-1,0),(0,-1),(0,1)]

    # Busca as posições de inicio (1) e fim (2)
    inicio = None
    fim = None
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 1:
                inicio = (i,j)
            if M[i][j] == 2:
                fim = (i,j)
    # Incializa a lista de caminhos
    L = [[inicio]]
    # Inicializa o conjunto de nós já visitados (utilizar set() garante busca em O(1))
    visited = set()

    # Loop principal da busca
    while L:   
        print(L)
        s = L.pop(-1) # Retira uma solução candidata da lista
        visited.add(s[-1]) # Adiciona o último nó da solução na lista de visitados

        if fim == s[-1]: # Verifica se s é um caminho de inicio a fim
            return True
        else:
            domain = [(s[-1][0] + d[0], s[-1][1] + d[1]) for d in directions] # Gera os possíveis vizinhos
            for e in domain: # Para cada vizinho e
                if e not in visited: # Verifica se e já não foi visitado
                    if e[0]>=0 and e[0]<len(M) and e[1]>=0 and e[1]<len(M[0]): # Verifica se e está dentro da matriz
                        if M[e[0]][e[1]] > 0: # Verifica se e é uma posição visitável (!= 0)
                            L.append(s + [e]) # Adiciona um novo caminho à lista

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