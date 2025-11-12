// DYNAMIC CODE: Prim's MST with user input and menu
#include <iostream>
#include <climits>
using namespace std;

#define MAX 10
int graph[MAX][MAX], V;

// Function to find the vertex with minimum key value
int minKey(int key[], bool mstSet[]) {
    int min = INT_MAX, min_index;
    for (int v = 0; v < V; v++)
        if (!mstSet[v] && key[v] < min)
            min = key[v], min_index = v;
    return min_index;
}

// Function to print the MST
void printMST(int parent[]) {
    cout << "\nMinimum Spanning Tree (Prim's):\n";
    for (int i = 1; i < V; i++)
        cout << "Dept " << parent[i] << " - Dept " << i << " : Distance = " << graph[i][parent[i]] << "\n";
}

// Prim’s algorithm
void primMST() {
    int parent[MAX], key[MAX];
    bool mstSet[MAX];

    for (int i = 0; i < V; i++)
        key[i] = INT_MAX, mstSet[i] = false;

    key[0] = 0;
    parent[0] = -1;

    for (int count = 0; count < V - 1; count++) {
        int u = minKey(key, mstSet);
        mstSet[u] = true;

        for (int v = 0; v < V; v++)
            if (graph[u][v] && !mstSet[v] && graph[u][v] < key[v])
                parent[v] = u, key[v] = graph[u][v];
    }

    printMST(parent);
}

// Main menu
int main() {
    int choice;
    cout << "Enter number of departments (nodes): ";
    cin >> V;

    cout << "\nEnter adjacency matrix (distance between departments):\n";
    for (int i = 0; i < V; i++)
        for (int j = 0; j < V; j++)
            cin >> graph[i][j];

    do {
        cout << "\n--- MENU ---\n";
        cout << "1. Display Adjacency Matrix\n";
        cout << "2. Find MST using Prim's Algorithm\n";
        cout << "3. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 1) {
            cout << "\nAdjacency Matrix:\n";
            for (int i = 0; i < V; i++) {
                for (int j = 0; j < V; j++)
                    cout << graph[i][j] << "\t";
                cout << "\n";
            }
        }
        else if (choice == 2) {
            primMST();
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
##sample Input =
Enter number of departments (nodes): 4

Enter adjacency matrix:
0 2 0 6
2 0 3 8
0 3 0 0
6 8 0 0
