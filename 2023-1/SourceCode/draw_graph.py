import networkx as nx
import matplotlib.pyplot as plt

def draw_graph_prim(graph, mst_edges=None):
    G = nx.Graph()

    # Add edges and weights to the graph
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors:
            G.add_edge(node, neighbor, weight=weight)

    # Get the positions of the nodes for better layout
    pos = nx.spring_layout(G)

    # Draw nodes
    nx.draw_networkx_nodes(G, pos)

    # Draw edges
    if mst_edges:
        mst_edges_set = set(mst_edges)
        non_mst_edges = [edge for edge in G.edges() if edge not in mst_edges_set]
        nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color='r', width=2.0)
        nx.draw_networkx_edges(G, pos, edgelist=non_mst_edges, edge_color='k', alpha=0.5)
    else:
        nx.draw_networkx_edges(G, pos)

    # Draw edge labels (weights)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Draw node labels
    nx.draw_networkx_labels(G, pos)

    # Show the graph
    plt.axis('off')
    plt.show()

def draw_graph_kruskall(graph, mst_edges):
    G = nx.Graph()

    # Add edges from the graph to the networkx graph object
    for vertex, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(vertex, neighbor, weight=weight)

    pos = nx.spring_layout(G)  # Layout algorithm for graph visualization

    # Draw graph edges
    nx.draw_networkx_edges(G, pos, alpha=0.2)

    # Highlight the edges in the MST
    nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color='r', width=2)

    # Draw graph nodes and labels
    nx.draw_networkx_nodes(G, pos, node_size=200, node_color='lightblue')
    nx.draw_networkx_labels(G, pos, font_size=10)

    # Draw edge labels
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Show the graph
    plt.axis('off')
    plt.show()