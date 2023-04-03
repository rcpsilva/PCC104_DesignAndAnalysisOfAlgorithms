#include<bits/stdc++.h>
using namespace std;

int main()
{
    int V = 5; // number of vertices in the graph

    vector<vector<int>> adj(V); // create an adjacency list with V vertices

    // initialize the adjacency list with hard-coded values
    adj[0] = {1, 4}; 
    adj[1] = {2};
    adj[2] = {3};
    adj[3] = {1};
    adj[4] = {3, 2};

    // print the adjacency list
    for (int i = 0; i < V; i++)
    {
        cout << i << " -> ";
        for (int j = 0; j < adj[i].size(); j++)
        {
            cout << adj[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}