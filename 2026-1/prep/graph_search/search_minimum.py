from heapq import *
from math import inf 

def inicializa(G,s):
   V = [{'id': i, 'cor':'B', 'pai':None, 'custo':inf} for i in range(len(G))] #[id,'Cor',Pai, Distância]
   V[s]['cor'] = 'C'
   V[s]['custo'] = 0
   return V

def relaxa(u,v,w):
   custo_relaxado = u['custo'] + w(u,v)
   if v['custo'] > custo_relaxado:
      v['custo'] = custo_relaxado
      v['pai'] = u


def dijkstra(G,w,s):
   V = inicializa(G,s)
   S = []
   Q = []
   for v_i in V:
      heappush(Q,(v_i['custo'],v_i)) 
   while Q:
      u = heappop(Q)
      S.append(u)
      for v_i in G[u['id']]:
         relaxa(V[u['id']],V[v_i],w)

   

