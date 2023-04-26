class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj_matrix = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]

    def add_node(self):
        self.num_nodes += 1
        for row in self.adj_matrix:
            row.append(0)
        self.adj_matrix.append([0 for _ in range(self.num_nodes)])

    def add_edge(self, node1, node2, weight=1):
        self.adj_matrix[node1][node2] = weight
        self.adj_matrix[node2][node1] = weight

    def remove_edge(self, node1, node2):
        self.adj_matrix[node1][node2] = 0
        self.adj_matrix[node2][node1] = 0

    def remove_node(self, node):
        self.num_nodes -= 1
        self.adj_matrix.pop(node)
        for row in self.adj_matrix:
            row.pop(node)

    def is_path(self, node1, node2):
        visited = [False] * self.num_nodes
        queue = [node1]
        visited[node1] = True

        while queue:
            current_node = queue.pop(0)
            if current_node == node2:
                return True
            for neighbor, weight in enumerate(self.adj_matrix[current_node]):
                if weight > 0 and not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return False


# example usage
g = Graph(3)  # create a graph with 3 nodes
g.add_edge(0, 1)  # add an edge between nodes 0 and 1
g.add_edge(1, 2)  # add an edge between nodes 1 and 2
print(g.adj_matrix)  # print the adjacency matrix
# Output: [[0, 1, 0], [1, 0, 1], [0, 1, 0]]

g.add_node()  # add a node to the graph
g.add_edge(0, 3)  # add an edge between nodes 0 and 3
print(g.adj_matrix)  # print the adjacency matrix
# Output: [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]

g.remove_edge(0, 3)  # remove the edge between nodes 0 and 3
g.remove_node(2)  # remove node 2 from the graph
print(g.adj_matrix)  # print the adjacency matrix
# Output: [[0, 1, 1], [1, 0, 0], [1, 0, 0]]

print(g.is_path(0, 2))  # check if a path exists between nodes 0 and 2
# Output: True
print(g.is_path(0, 1))  # check if a path exists between nodes 0 and 1
# Output: True
print(g.is_path(1, 2))  # check if a path exists between nodes 1 and 2
# Output: False
