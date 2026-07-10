"""
Demonstração passo a passo do algoritmo de Dijkstra (CLRS),
com instrumentação do conjunto S e visualização gráfica de cada iteração.

Estrutura fiel ao pseudocódigo:
    INITIALIZE-SINGLE-SOURCE(G,s)
    S = vazio ; Q = G.V
    enquanto Q != vazio:
        u = EXTRACT-MIN(Q)
        S = S U {u}
        para v em G.Adj[u]: RELAX(u,v,w)
"""

import math
from heapq import heappush, heappop

import matplotlib.pyplot as plt
import networkx as nx


# ----------------------------------------------------------------------
# 1. Algoritmo instrumentado: em vez de só calcular o resultado final,
#    guarda um "snapshot" do estado (S, Q, d, pai) a cada iteração.
# ----------------------------------------------------------------------

def inicializa(G, s):
    V = [{'id': i, 'pai': None, 'custo': math.inf} for i in range(len(G))]
    V[s]['custo'] = 0
    return V


def relaxa(u, v, w):
    custo_relaxado = u['custo'] + w(u['id'], v['id'])
    if v['custo'] > custo_relaxado:
        v['custo'] = custo_relaxado
        v['pai'] = u['id']
        return True
    return False


def dijkstra(G, w, s):
    V = inicializa(G, s)
    S = set()
    Q = [(0, s)]           # push por id, não pelo dict
    historico = []
    while Q:
      custo_u, u_id = heappop(Q)
      if u_id not in S:    
         S.add(u_id)
         u = V[u_id]
         for v_id in G[u_id]:
            v = V[v_id]
            if v_id not in S and relaxa(u, v, w):
               heappush(Q, (v['custo'], v_id))

         historico.append({
                'u': u_id,
                'S': set(S),
                'd': [x['custo'] for x in V],
                'pai': [x['pai'] for x in V],
            })
    return V, historico


def dijkstra_instrumentado(G, w, s):
    """
    Executa Dijkstra e retorna (V_final, historico), onde historico é uma
    lista de snapshots, um por vértice extraído, contendo:
        {'u': id extraído, 'S': set já finalizado (após incluir u),
         'd': lista de custos correntes, 'pai': lista de pais correntes,
         'relaxados': lista de (v_id, melhorou?) tentados nesta iteração}
    """
    V = inicializa(G, s)
    S = set()
    Q = [(0, s)]
    historico = []

    while Q:
        custo_u, u_id = heappop(Q)
        if u_id in S:
            continue  # entrada obsoleta (lazy deletion, sem decrease-key)
        S.add(u_id)
        u = V[u_id]

        relaxados = []
        for v_id in G[u_id]:
            v = V[v_id]
            if v_id in S:
                continue
            melhorou = relaxa(u, v, w)
            if melhorou:
                heappush(Q, (v['custo'], v_id))
            relaxados.append((v_id, melhorou))

            historico.append({
                'u': u_id,
                'S': set(S),
                'd': [x['custo'] for x in V],
                'pai': [x['pai'] for x in V],
                'relaxados': relaxados,
            })

    return V, historico


# ----------------------------------------------------------------------
# 2. Visualização textual (tabela no terminal, a cada iteração)
# ----------------------------------------------------------------------

def imprime_passo(passo_num, snap, n):
    u = snap['u']
    print(f"\n--- Iteração {passo_num}: extraído u = {u} ---")
    print(f"S = {sorted(snap['S'])}")
    #for v_id, melhorou in snap['relaxados']:
    #    status = "melhorou" if melhorou else "sem alteração"
    #    print(f"  relaxa({u} -> {v_id}): {status}")
    print("id | d   | pai")
    for i in range(n):
        d = snap['d'][i]
        d_str = "inf" if d == math.inf else str(d)
        print(f" {i}  | {d_str:>3} | {snap['pai'][i]}")


# ----------------------------------------------------------------------
# 3. Visualização gráfica (um painel por iteração, com networkx)
# ----------------------------------------------------------------------

def desenha_grafo(ax, G_nx, pos, pesos, snap, s, n, passo_num):
    S = snap['S']
    u_id = snap['u']
    d = snap['d']
    pai = snap['pai']

    cores = []
    for i in range(n):
        if i == u_id:
            cores.append('#f4a300')       # laranja: vértice recém-finalizado
        elif i in S:
            cores.append('#4c72b0')       # azul: já em S (finalizado antes)
        else:
            cores.append('#dddddd')       # cinza claro: ainda em Q

    # arestas da árvore de caminhos mínimos construída até agora
    arestas_arvore = [(pai[i], i) for i in range(n) if pai[i] is not None]

    nx.draw_networkx_edges(G_nx, pos, ax=ax, edge_color='#cccccc', arrows=True)
    nx.draw_networkx_edges(G_nx, pos, ax=ax, edgelist=arestas_arvore,
                            edge_color='#f4a300', width=2.5, arrows=True)
    nx.draw_networkx_labels(G_nx, pos, ax=ax, font_size=9, font_color='white')
    nx.draw_networkx_nodes(G_nx, pos, ax=ax, node_color=cores,
                            node_size=600, edgecolors='black')
    nx.draw_networkx_edge_labels(G_nx, pos, ax=ax, edge_labels=pesos, font_size=7)

    labels_d = {i: ("∞" if d[i] == math.inf else str(d[i])) for i in range(n)}
    pos_labels = {i: (x, y + 0.14) for i, (x, y) in pos.items()}
    for i in range(n):
        ax.text(pos_labels[i][0], pos_labels[i][1], f"d={labels_d[i]}",
                ha='center', fontsize=8)

    titulo = f"Passo {passo_num}: u = {u_id}  |  S = {sorted(S)}"
    ax.set_title(titulo, fontsize=9)
    ax.axis('off')


def visualiza_execucao(G, w, s, historico, arquivo_saida="dijkstra_passos.png"):
    n = len(G)
    G_nx = nx.DiGraph()
    G_nx.add_nodes_from(range(n))
    pesos = {}
    for u in range(n):
        for v in G[u]:
            peso = w(u, v)
            G_nx.add_edge(u, v, weight=peso)
            pesos[(u, v)] = peso

    pos = nx.spring_layout(G_nx, seed=42)

    n_passos = len(historico)
    ncols = min(3, n_passos)
    nrows = math.ceil(n_passos / ncols)
    fig, axes = plt.subplots(nrows, ncols, figsize=(5 * ncols, 4.5 * nrows))
    axes = axes.flatten() if n_passos > 1 else [axes]

    for i, snap in enumerate(historico):
        desenha_grafo(axes[i], G_nx, pos, pesos, snap, s, n, i + 1)

    for j in range(len(historico), len(axes)):
        axes[j].axis('off')

    fig.suptitle(f"Execução do Dijkstra a partir de s={s}", fontsize=12)
    fig.tight_layout()
    fig.savefig(arquivo_saida, dpi=150, bbox_inches='tight')
    print(f"\nFigura salva em: {arquivo_saida}")


# ----------------------------------------------------------------------
# 4. Exemplo mínimo (o mesmo grafo usado na explicação anterior)
# ----------------------------------------------------------------------

if __name__ == "__main__":
    # G[u] = lista de vizinhos de u (grafo dirigido)
    G = {
        0: [1,2],
        1: [2,3],
        2: [4,3,1],
        3: [4],
        4: [0,3],
    }
    pesos_arestas = {
        (0, 1): 10,
        (0, 2): 5,
        (1, 2): 2,
        (1, 3): 1,
        (2, 1): 3,
        (2, 3): 9,
        (2, 4): 2,
        (3, 4): 4,
        (4, 0): 7,
        (4, 3): 6
        
    }

    def w(u_id, v_id):
        return pesos_arestas[(u_id, v_id)]

    s = 0
    V_final, historico = dijkstra(G, w, s)

    print("=" * 50)
    print("EXECUÇÃO PASSO A PASSO")
    print("=" * 50)
    for i, snap in enumerate(historico):
        imprime_passo(i + 1, snap, len(G))

    print("\n" + "=" * 50)
    print("RESULTADO FINAL")
    print("=" * 50)
    for v in V_final:
        d = "inf" if v['custo'] == math.inf else v['custo']
        print(f"  vértice {v['id']}: d={d}, pai={v['pai']}")

    visualiza_execucao(G, w, s, historico,
                        arquivo_saida="dijkstra_passos.png")