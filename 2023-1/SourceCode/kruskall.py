from draw_graph import draw_graph

def kruskal(graph):
    # Collect all edges from the graph
    edges = []
    for vertex, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            edges.append((vertex, neighbor, weight))

    # Sort edges in non-decreasing order of weights
    edges.sort(key=lambda x: x[2])

    ET = []  # Set of edges composing the minimum spanning tree
    ecounter = 0  # Counter for the size of the tree edges
    k = 0  # Counter for processed edges

    parent = {}  # Dictionary to track parent of each vertex
    rank = {}  # Dictionary to track rank (depth) of each vertex

    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(v1, v2):
        root1 = find(v1)
        root2 = find(v2)
        if root1 != root2:
            if rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                if rank[root1] == rank[root2]:
                    rank[root1] += 1

    # Initialize parent and rank dictionaries
    for vertex in graph.keys():
        parent[vertex] = vertex
        rank[vertex] = 0

    while ecounter < len(graph) - 1:
        k += 1
        v1, v2, weight = edges[k]
        if find(v1) != find(v2):  # Check if adding edge creates a cycle
            union(v1, v2)  # Merge the disjoint sets of v1 and v2
            ET.append((v1, v2, weight))  # Add the edge to the MST
            ecounter += 1

    return ET


# Example usage
graph = {
    'A': {'B': 4, 'H': 8},
    'B': {'A': 4, 'H': 11, 'C': 8},
    'C': {'B': 8, 'I': 2, 'F': 4, 'D': 7},
    'D': {'C': 7, 'F': 14, 'E': 9},
    'E': {'D': 9, 'F': 10},
    'F': {'C': 4, 'D': 14, 'E': 10, 'G': 2},
    'G': {'F': 2, 'I': 6, 'H': 1},
    'H': {'A': 8, 'B': 11, 'G': 1, 'I': 7},
    'I': {'C': 2, 'G': 6, 'H': 7}
}

minimum_spanning_tree = kruskal(graph)
for edge in minimum_spanning_tree:
    print(edge)

draw_graph(graph,minimum_spanning_tree)