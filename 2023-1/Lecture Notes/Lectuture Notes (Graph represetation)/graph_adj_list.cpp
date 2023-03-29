#include <iostream>
#include <unordered_map>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

class Graph {
private:
    unordered_map<string, vector<pair<string, int>>> adj_list;

public:
    void add_node(string node) {
        if (adj_list.find(node) == adj_list.end()) {
            adj_list[node] = {};
        }
    }

    void add_edge(string node1, string node2, int weight = 1) {
        add_node(node1);
        add_node(node2);
        adj_list[node1].push_back({node2, weight});
        adj_list[node2].push_back({node1, weight});
    }

    void remove_edge(string node1, string node2) {
        auto it = find_if(adj_list[node1].begin(), adj_list[node1].end(),
                          [node2](const pair<string, int>& p) {
                              return p.first == node2;
                          });
        if (it != adj_list[node1].end()) {
            adj_list[node1].erase(it);
        }
        it = find_if(adj_list[node2].begin(), adj_list[node2].end(),
                     [node1](const pair<string, int>& p) {
                         return p.first == node1;
                     });
        if (it != adj_list[node2].end()) {
            adj_list[node2].erase(it);
        }
    }

    void remove_node(string node) {
        adj_list.erase(node);
        for (auto& [other_node, neighbours] : adj_list) {
            auto it = find_if(neighbours.begin(), neighbours.end(),
                              [node](const pair<string, int>& p) {
                                  return p.first == node;
                              });
            if (it != neighbours.end()) {
                neighbours.erase(it);
            }
        }
    }

    bool is_path(string node1, string node2) {
        unordered_set<string> visited;
        stack<string> st;
        st.push(node1);
        while (!st.empty()) {
            string node = st.top();
            st.pop();
            if (node == node2) {
                return true;
            }
            if (visited.find(node) == visited.end()) {
                visited.insert(node);
                for (auto& [neighbour, weight] : adj_list[node]) {
                    st.push(neighbour);
                }
            }
        }
        return false;
    }
};

int main() {
    Graph g;
    g.add_edge("A", "B"); // add an edge between nodes 'A' and 'B'
    g.add_edge("B", "C"); // add an edge between nodes 'B' and 'C'
    for (auto& [node, neighbours] : g.adj_list) {
        cout << node << ": ";
        for (auto& [neighbour, weight] : neighbours) {
            cout << "(" << neighbour << ", " << weight << ") ";
        }
        cout << endl;
    }
    // Output: A: (B, 1)
    //         B: (A, 1) (C, 1)
    //         C: (B, 1)

    g.add_edge("A", "D"); // add an edge between nodes 'A' and 'D'
    for (auto& [node, neighbours] : g.adj_list) {
        cout << node << ": ";
        for (auto& [neighbour, weight] : neighbours) {
            cout << "(" << neighbour << ", " << weight << ") ";
        }
        cout << endl;
    }
}