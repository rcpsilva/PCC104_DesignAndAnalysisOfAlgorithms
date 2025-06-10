def bfs(G, start, target):

    #visited = {node:parent)}
    visited = {start:''}
    F = [start]

    while F:
        print(F)
        node = F.pop(0)

        if node == target:
            return node, visited

        for n in G[node]:
            if n not in visited:
                F.append(n)
                visited[n] = node

def dfs(G, start, target):

    #visited = {node:parent)}
    visited = {start:''}
    F = [start]

    while F:
        print(F)
        node = F.pop()

        if node == target:
            return node, visited

        for n in G[node]:
            if n not in visited:
                F.append(n)
                visited[n] = node
    

def recover_path(node,visited):

    path = [node]

    while visited[node] != '':
        parent = visited[node] 
        path = [parent] + path
        node = parent

    return path

if __name__ == '__main__':

    G = {'A':['B','C','D'],
         'B':['E','F','G'],
         'C':[],
         'D':[],
         'E':[],
         'F':[],
         'G':['H'],
         'H':[],}
    
    node, visited = bfs(G,'A','H')

    print(f'path: {recover_path(node,visited)}')