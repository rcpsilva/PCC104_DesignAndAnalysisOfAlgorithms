from heapq import heappush, heappop
import math

def inicializa(G, s):
    V = [{'id': i, 'pai': None, 'custo': math.inf} for i in range(len(G))]
    V[s]['custo'] = 0
    return V

def relaxa(u, v, w):
    custo_relaxado = u['custo'] + w(u, v)
    if v['custo'] > custo_relaxado:
        v['custo'] = custo_relaxado
        v['pai'] = u
        return True
    return False

def dijkstra(G, w, s):
    V = inicializa(G, s)
    S = set()
    Q = [(0, s)]           # push por id, não pelo dict
    while Q:
      custo_u, u_id = heappop(Q)
      if u_id not in S:    
         S.add(u_id)
         u = V[u_id]
         for v_id in G[u_id]:
            v = V[v_id]
            if v_id not in S and relaxa(u, v, w):
               heappush(Q, (v['custo'], v_id))
    return V

