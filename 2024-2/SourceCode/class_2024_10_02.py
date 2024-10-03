# 'Busca em Largura' para gerar todas a permutações
def bfs_perm(domain):
    n = len(domain)
    L = []
    
    for e in domain:
        L.append([e])
    
    while L:
        s = L.pop(0)

        if len(s) == n:
            print(s)
        else:
            for e in domain:
                if e not in s:
                    L.append(s + [e])

# 'Busca em largura' para gerar todas as combinações
def bfs(n, domain):
    L = []
    for e in domain:
        L.append([e])
    while L:
        s = L.pop(0)

        if len(s) == n:
            print(s)
        else:
            for e in domain:
                L.append(s + [e])

if __name__ == '__main__':
    
    bfs_perm([0,1,2,3])