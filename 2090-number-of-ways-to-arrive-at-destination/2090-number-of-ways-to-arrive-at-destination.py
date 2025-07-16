import heapq
from collections import defaultdict


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # Step 1: Create adjacency list
        adj = [[] for _ in range(n)]
        for u, v, wt in roads:
            adj[u].append((v, wt))
            adj[v].append((u, wt))

        # Step 2: Initialize distance and ways array
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        mod = 10**9 + 7

        # Step 3: Min-heap as priority queue: (distance, node)
        pq = [(0, 0)]  # (distance, node)

        # Step 4: Dijkstra-like traversal
        while pq:
            dis, node = heapq.heappop(pq)

            for neighbor, wt in adj[node]:
                if dis + wt < dist[neighbor]:
                    dist[neighbor] = dis + wt
                    ways[neighbor] = ways[node]
                    heapq.heappush(pq, (dist[neighbor], neighbor))
                elif dis + wt == dist[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % mod

        return ways[n - 1] % mod
