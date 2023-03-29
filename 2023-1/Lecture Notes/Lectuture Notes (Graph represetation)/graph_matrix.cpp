#include <iostream>
#include <vector>
using namespace std;

class Graph {
public:
    Graph(int num_nodes) : num_nodes(num_nodes), adj_matrix(num_nodes, vector<int>(num_nodes, 0)) {}

    void add_node() {
        num_nodes++;
        for (auto& row : adj_matrix) {
            row.push_back(0);
        }
        adj_matrix.push_back(vector<int>(num_nodes, 0));
    }

    void add_edge(int node1, int node2, int weight = 1) {
        adj_matrix[node1][node2] = weight;
        adj_matrix[node2][node1] = weight;
    }

    void remove_edge(int node1, int node2) {
        adj_matrix[node1][node2] = 0;
        adj_matrix[node2][node1] = 0;
    }

    void remove_node(int node) {
        num_nodes--;
        adj_matrix.erase(adj_matrix.begin() + node);
        for (auto& row : adj_matrix) {
            row.erase(row.begin() + node);
        }
    }

    bool is_path(int node1, int node2) {
        vector<bool> visited(num_nodes, false);
        vector<int> queue;
        queue.push_back(node1);
        visited[node1] = true;

        while (!queue.empty()) {
            int current_node = queue.front();
            queue.erase(queue.begin());
            if (current_node == node2) {
                return true;
            }
            for (int neighbor = 0; neighbor < num_nodes; neighbor++) {
                int weight = adj_matrix[current_node][neighbor];
                if (weight > 0 && !visited[neighbor]) {
                    visited[neighbor] = true;
                    queue.push_back(neighbor);
                }
            }
        }

        return false;
    }

private:
    int num_nodes;
    vector<vector<int>> adj_matrix;
};

int main() {
    Graph g(3);  // create a graph with 3 nodes
    g.add_edge(0, 1);  // add an edge between nodes 0 and 1
    g.add_edge(1, 2);  // add an edge between nodes 1 and 2
    for (auto row : g.adj_matrix) {
        for (auto val : row) {
            cout << val << " ";
        }
        cout << endl;
    }  // print the adjacency matrix
    // Output: 0 1 0
    //         1 0 1
    //         0 1 0

    g.add_node();  // add a node to the graph
    g.add_edge(0, 3);  // add an edge between nodes 0 and 3
    for (auto row : g.adj_matrix) {
        for (auto val : row) {
            cout << val << " ";
        }
        cout << endl;
    }  // print the adjacency matrix
    // Output: 0 1 0 1
    //         1 0 1 0
    //         0 1 0 0
    //         1 0 0 0

    g.remove_edge(0, 3);  // remove the edge between nodes 0 and 3
    g.remove_node(2);  // remove node 2 from the graph
    for (auto row : g.adj_matrix) {
        for (auto val : row) {
            cout << val << " ";
        }
        cout << endl;
    }  // print the adjacency matrix
} 
