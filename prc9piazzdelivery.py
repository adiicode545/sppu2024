# tsp_solutions.py
from itertools import combinations
import math
import random
import heapq

# ---------- Utility: make complete distance matrix via Dijkstra ----------
def floyd_warshall(adj_matrix):
    # adj_matrix: n x n, with math.inf for no direct edge
    n = len(adj_matrix)
    dist = [row[:] for row in adj_matrix]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

# ---------- 1) Held-Karp exact TSP ----------
def held_karp(dist, start=0):
    # dist: n x n matrix (complete), start: index of shop
    n = len(dist)
    ALL = 1 << n
    # dp[mask][i] = min cost to reach set mask finishing at i
    dp = [dict() for _ in range(ALL)]
    prev = [dict() for _ in range(ALL)]
    start_mask = 1 << start
    dp[start_mask][start] = 0

    for mask in range(ALL):
        if not (mask & start_mask): 
            continue
        for u, cost_u in dp[mask].items():
            for v in range(n):
                if mask & (1 << v):
                    continue
                new_mask = mask | (1 << v)
                new_cost = cost_u + dist[u][v]
                if v not in dp[new_mask] or new_cost < dp[new_mask][v]:
                    dp[new_mask][v] = new_cost
                    prev[new_mask][v] = u

    full_mask = (1 << n) - 1
    # If we require returning to start:
    best_cost = math.inf
    best_end = None
    for v, c in dp[full_mask].items():
        total = c + dist[v][start]  # close the loop
        if total < best_cost:
            best_cost = total
            best_end = v

    if best_end is None:
        return None, math.inf

    # Reconstruct path
    path = []
    mask = full_mask
    cur = best_end
    while mask != start_mask or cur != start:
        path.append(cur)
        prev_cur = prev[mask].get(cur, None)
        mask ^= (1 << cur)
        cur = prev_cur
    path.append(start)
    path.reverse()
    return path, best_cost

# ---------- 2) Nearest Neighbor + 2-opt ----------
def nearest_neighbor(dist, start=0):
    n = len(dist)
    unvisited = set(range(n))
    path = [start]
    unvisited.remove(start)
    current = start
    while unvisited:
        nxt = min(unvisited, key=lambda x: dist[current][x])
        path.append(nxt)
        unvisited.remove(nxt)
        current = nxt
    # optionally return to start if required:
    # path.append(start)
    return path

def path_cost(path, dist, return_to_start=True):
    cost = 0
    for i in range(len(path)-1):
        cost += dist[path[i]][path[i+1]]
    if return_to_start:
        cost += dist[path[-1]][path[0]]
    return cost

def two_opt(path, dist, max_iter=1000):
    # path is list of node indices (assume cycle if return_to_start)
    n = len(path)
    best = path[:]
    improved = True
    it = 0
    while improved and it < max_iter:
        improved = False
        it += 1
        for i in range(1, n-2):
            for j in range(i+1, n):
                if j - i == 1:
                    continue
                new_path = best[:]
                new_path[i:j] = reversed(best[i:j])
                if path_cost(new_path, dist) < path_cost(best, dist):
                    best = new_path
                    improved = True
        # optionally break early
    return best

def nearest_neighbor_with_2opt(dist, start=0):
    p = nearest_neighbor(dist, start)
    # make it a cycle by appending start for cost calculations if needed
    cost_before = path_cost(p, dist)
    p2 = two_opt(p, dist)
    cost_after = path_cost(p2, dist)
    return p2, cost_after

# ---------- Example usage ----------
if __name__ == "__main__":
    # Example: 5 nodes (0=shop, 1..4 customers)
    # Use large value math.inf to indicate no direct edge
    inf = float('inf')
    road_adj = [
        [0, 10, inf, 30, 100],
        [10, 0, 50, inf, inf],
        [inf, 50, 0, 20, 10],
        [30, inf, 20, 0, 60],
        [100, inf, 10, 60, 0]
    ]
    # Make complete by computing all-pairs shortest paths
    dist = floyd_warshall(road_adj)

    # Exact (if small)
    path, cost = held_karp(dist, start=0)
    print("Held-Karp optimal cycle:", path, "cost=", cost)

    # Heuristic
    hpath, hcost = nearest_neighbor_with_2opt(dist, start=0)
    print("Heuristic cycle:", hpath, "cost=", hcost)
