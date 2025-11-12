// DYNAMIC CODE: Kruskal's MST with user input and menu
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Edge {
    int u, v, weight;
};

bool compare(Edge a, Edge b) {
    return a.weight < b.weight;
}

int findParent(int node, vector<int>& parent) {
    if (parent[node] == node)
        return node;
    return parent[node] = findParent(parent[node], parent);
}

void unionSets(int u, int v, vector<int>& parent) {
    int pu = findParent(u, parent);
    int pv = findParent(v, parent);
    if (pu != pv)
        parent[pu] = pv;
}

void kruskalMST(vector<Edge>& edges, int V) {
    sort(edges.begin(), edges.end(), compare);
    vector<int> parent(V);
    for (int i = 0; i < V; i++)
        parent[i] = i;

    vector<Edge> mst;
    for (Edge e : edges) {
        if (findParent(e.u, parent) != findParent(e.v, parent)) {
            mst.push_back(e);
            unionSets(e.u, e.v, parent);
        }
    }

    cout << "\nMinimum Spanning Tree (Kruskal's):\n";
    for (Edge e : mst)
        cout << "Dept " << e.u << " - Dept " << e.v << " : Distance = " << e.weight << "\n";
}

int main() {
    int V, E, choice;
    vector<Edge> edges;

    cout << "Enter number of departments (nodes): ";
    cin >> V;

    cout << "Enter number of connections (edges): ";
    cin >> E;

    cout << "\nEnter edges (format: dept1 dept2 distance):\n";
    for (int i = 0; i < E; i++) {
        Edge e;
        cin >> e.u >> e.v >> e.weight;
        edges.push_back(e);
    }

    do {
        cout << "\n--- MENU ---\n";
        cout << "1. Display Edge List\n";
        cout << "2. Find MST using Kruskal's Algorithm\n";
        cout << "3. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 1) {
            cout << "\nEdge List:\n";
            for (Edge e : edges)
                cout << "Dept " << e.u << " - Dept " << e.v << " : Distance = " << e.weight << "\n";
        }
        else if (choice == 2) {
            kruskalMST(edges, V);
        }
        else if (choice == 3) {
            cout << "Exiting...\n";
        }
        else {
            cout << "Invalid choice. Try again.\n";
        }
    } while (choice != 3);

    return 0;
}
#Sample input
Enter number of departments (nodes): 4
Enter number of connections (edges): 5

Enter edges:
0 1 10
0 2 6
0 3 5
1 3 15
2 3 4 
