# -------- DFS using Adjacency Matrix --------
def dfs(matrix, visited, node):
    print(node, end=" ")
    visited[node] = True
    for i in range(len(matrix)):
        if matrix[node][i] == 1 and not visited[i]:
            dfs(matrix, visited, i)

# -------- BFS using Adjacency List --------
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Node mapping for adjacency matrix
nodes = ['A', 'B', 'C', 'D', 'E']
adj_matrix = [
    [0,1,1,0,0],
    [1,0,0,1,0],
    [1,0,0,1,1],
    [0,1,1,0,1],
    [0,0,1,1,0]
]

# DFS traversal
print("DFS Traversal (Adjacency Matrix):")
visited = [False]*len(nodes)
dfs(adj_matrix, visited, 0)   # Start from 'A' (index 0)

# Adjacency list for BFS
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}

# BFS traversal
print("\n\nBFS Traversal (Adjacency List):")
bfs(graph, 'A')
