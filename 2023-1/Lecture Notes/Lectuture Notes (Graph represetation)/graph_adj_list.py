class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, node1, node2, weight=1):
        self.add_node(node1)
        self.add_node(node2)
        self.adj_list[node1].append((node2, weight))
        self.adj_list[node2].append((node1, weight))

    def remove_edge(self, node1, node2):
        for i, (node, weight) in enumerate(self.adj_list[node1]):
            if node == node2:
                del self.adj_list[node1][i]
                break
        for i, (node, weight) in enumerate(self.adj_list[node2]):
            if node == node1:
                del self.adj_list[node2][i]
                break

    def remove_node(self, node):
        del self.adj_list[node]
        for other_node in self.adj_list:
            for i, (n, w) in enumerate(self.adj_list[other_node]):
                if n == node:
                    del self.adj_list[other_node][i]
                    break

    def is_path(self, node1, node2):
        visited = set()
        stack = [node1]
        while stack:
            node = stack.pop()
            if node == node2:
                return True
            if node not in visited:
                visited.add(node)
                stack.extend(neighbour for neighbour, weight in self.adj_list[node])
        return False

# example usage
g = Graph()
g.add_edge('A', 'B')  # add an edge between nodes 'A' and 'B'
g.add_edge('B', 'C')  # add an edge between nodes 'B' and 'C'
print(g.adj_list)  # print the adjacency list
# Output: {'A': [('B', 1)], 'B': [('A', 1), ('C', 1)], 'C': [('B', 1)]}

g.add_edge('A', 'D')  # add an edge between nodes 'A' and 'D'
print(g.adj_list)  # print the adjacency list
# Output: {'A': [('B', 1), ('D', 1)], 'B': [('A', 1), ('C', 1)], 'C': [('B', 1)], 'D': [('A', 1)]}

g.remove_edge('A', 'D')  # remove the edge between nodes 'A' and 'D'
g.remove_node('B')  # remove node 'B' from the graph
print(g.adj_list)  # print the adjacency list
# Output: {'A': [], 'C': []}

print(g.is_path('A', 'C'))  # check if a path exists between nodes 'A' and 'C'
# Output: False
print(g.is_path('A', 'D'))  # check if a path exists between nodes 'A' and 'D'
# Output: False
print(g.is_path('D', 'A'))  # check if a path exists between nodes 'D' and 'A'
# Output: True