class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:


        # Build adjacency list: node -> list of (neighbor, weight)
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))

        # Queue will store (stops_so_far, current_node, current_cost)
        q = deque()
        q.append((0, src, 0))

        # Distance array to store minimum cost to each node
        dist = [float('inf')] * n
        dist[src] = 0

        while q:
            stops, node, cost = q.popleft()

            # If number of stops exceeds limit, skip
            if stops > k:
                continue

            # Traverse adjacent nodes
            for neighbor, price in adj[node]:
                if cost + price < dist[neighbor]:
                    dist[neighbor] = cost + price
                    q.append((stops + 1, neighbor, cost + price))

        return -1 if dist[dst] == float('inf') else dist[dst]

        