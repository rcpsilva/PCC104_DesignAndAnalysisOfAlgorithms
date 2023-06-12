from collections import defaultdict
import heapq
from draw_graph import draw_graph_prim

def prim(graph):
    # Select an arbitrary starting vertex
    start_vertex = next(iter(graph))

    # Maintain a set to keep track of visited vertices
    visited = set([start_vertex])

    # Initialize the minimum spanning tree and the priority queue
    mst = []
    pq = [(weight, start_vertex, neighbor) for neighbor, weight in graph[start_vertex]]

    # Use a heap to efficiently retrieve the edge with the minimum weight
    heapq.heapify(pq)

    while pq:
        weight, current_vertex, next_vertex = heapq.heappop(pq)

        if next_vertex not in visited:
            visited.add(next_vertex)
            mst.append((current_vertex, next_vertex, weight))

            for neighbor, weight in graph[next_vertex]:
                if neighbor not in visited:
                    heapq.heappush(pq, (weight, next_vertex, neighbor))

    return mst


# Example usage
graph = {}
graph['A'] = [('B', 4), ('H', 8)]
graph['B'] = [('A', 4), ('H', 11), ('C', 8)]
graph['C'] = [('B', 8), ('I', 2), ('F', 4), ('D', 7)]
graph['D'] = [('C', 7), ('F', 14), ('E', 9)]
graph['E'] = [('D', 9), ('F', 10)]
graph['F'] = [('C', 4), ('D', 14), ('E', 10), ('G', 2)]
graph['G'] = [('F', 2), ('I', 6), ('H', 1)]
graph['H'] = [('A', 8), ('B', 11), ('G', 1), ('I', 7)]
graph['I'] = [('C', 2), ('G', 6), ('H', 7)]


minimum_spanning_tree = prim(graph)
for edge in minimum_spanning_tree:
    print(edge)

draw_graph_prim(graph,minimum_spanning_tree)