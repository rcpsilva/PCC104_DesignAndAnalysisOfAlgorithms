import random
import matplotlib.pyplot as plt
from scipy.spatial import distance

def generate_points(m):
    points = []
    for _ in range(m):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        points.append((x, y))
    return points

def generate_graph(n):
    graph = {i: [] for i in range(n)}
    
    for i in range(n):
        for j in range(i+1, n):
            if random.random() < 0.3:
                graph[i].append(j)
                graph[j].append(i)
    
    return graph

def randomized_prim(points):
    n = len(points)
    start_node = random.randint(0, n-1)
    visited = [False] * n
    visited[start_node] = True

    edges = []
    while len(edges) < n - 1:
        eligible_edges = []
        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if not visited[j]:
                        dist = distance.euclidean(points[i], points[j])
                        eligible_edges.append((dist, i, j))
        eligible_edges.sort()
        _, u, v = random.choice(eligible_edges)
        edges.append((u, v))
        visited[v] = True

    return edges

def edges_to_adjacency_list(edges):
    adjacency_list = {}
    for u, v in edges:
        adjacency_list.setdefault(u, []).append(v)
        adjacency_list.setdefault(v, []).append(u)
    return adjacency_list

def draw_graph(points, edges):
    for i, point in enumerate(points):
        plt.scatter(point[0], point[1], color='blue')
    for u, v in edges:
        plt.plot([points[u][0], points[v][0]], [points[u][1], points[v][1]], color='black')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Random Spanning Tree Visualization')
    plt.show()

def plot_path(path, points, edges, begin, end):

    for i, point in enumerate(points):
        plt.scatter(point[0], point[1], color='black')
    for u, v in edges:
        plt.plot([points[u][0], points[v][0]], [points[u][1], points[v][1]], color='black')
    
    for i in range(len(path)-1):
        p1 = points[path[i]]
        p2 = points[path[i+1]]
        plt.plot([p1[0],p2[0]],[p1[1],p2[1]], '-r')

    plt.plot(points[begin][0],points[begin][1],'ob')
    plt.plot(points[end][0],points[end][1],'or')
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Random Spanning Tree Visualization')
    plt.show()

def graph_to_edges(graph):
    edges = set()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            edge = tuple(sorted((node, neighbor)))
            edges.add(edge)
    return edges

def get_cost(points,path):
    cost = 0
    for i in range(len(path)-1):
        cost += distance.euclidean(points[path[i]],points[path[i+1]])

    return cost


def df(points, graph, begin, end):

    F = [[begin]]

    while F:
        path = F.pop()
        
        if path[-1] == end:
            return path
        
        for neighbor in graph[path[-1]]:
            if neighbor not in path:
                F.append(path + [neighbor])

    return

def bb(points, graph, begin, end, bound=10000):

    F = [[begin]]
    C = [0]
    H = [distance.euclidean(points[begin],points[end])]

    best_path = []
    best_cost = bound

    while F:
        path = F.pop()
        cost = C.pop()
        heu = H.pop()

        if cost + heu < bound:
            
            if path[-1] == end:
                print(bound)
                if cost < best_cost:
                    best_path = path
                    best_cost = cost
                    bound = cost

            else:
                for neighbor in graph[path[-1]]:
                    if neighbor not in path:
                        F.append(path + [neighbor])
                        C.append(cost + distance.euclidean(points[path[-1]],points[neighbor]))
                        H.append(distance.euclidean(points[neighbor],points[end]))

    return best_path



if __name__ == '__main__':

    # Example usage
    m = 15
    points = generate_points(m)
    graph = generate_graph(m)

    print(points)
    print(graph)

    begin = 0
    end = 1

    path = bb(points,graph,begin,end)

    print(path)
    print(get_cost(points,path))

    # Draw the random spanning tree
    plot_path(path, points, graph_to_edges(graph), begin, end)



