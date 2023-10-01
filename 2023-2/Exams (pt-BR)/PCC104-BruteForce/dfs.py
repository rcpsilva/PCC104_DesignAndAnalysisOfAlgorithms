def dfs(graph, start_vertex, visited=set()):
    visited.add(start_vertex)
    print(start_vertex, end=' ')

    for neighbor in graph[start_vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example usage:
# Define an adjacency list representation of the graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_vertex = 'A'
print("DFS traversal starting from vertex 'A':")
dfs(graph, start_vertex)
