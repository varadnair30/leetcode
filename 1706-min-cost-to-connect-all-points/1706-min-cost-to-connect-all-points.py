import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:


        V = len(points)

        # Step 1: Build the adjacency list using Manhattan distance
        adj = [[] for _ in range(V)]
        for i in range(V):
            x1, y1 = points[i]
            for j in range(i+1, V):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([j, dist])
                adj[j].append([i, dist])

        # Step 2: Use the standard Prim’s logic
        return self.spanningTree(V, adj)

    # Prim's Algorithm
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        vis = [0] * V
        min_Heap = [(0, 0)]  # (weight, node)
        mst_weight = 0

        while min_Heap:
            wt, node = heapq.heappop(min_Heap)

            if vis[node]:
                continue

            vis[node] = 1
            mst_weight += wt

            for neighbor in adj[node]:
                adj_node = neighbor[0]
                edge_weight = neighbor[1]

                if not vis[adj_node]:
                    heapq.heappush(min_Heap, (edge_weight, adj_node))

        return mst_weight





        