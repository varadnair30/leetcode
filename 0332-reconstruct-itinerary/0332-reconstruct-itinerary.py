import heapq

class Solution:
    def findItinerary(self, tickets):
        adj = defaultdict(list)
        for u, v in tickets:
            heapq.heappush(adj[u], v)

        res = []
        def dfs(node):
            while adj[node]:
                dfs(heapq.heappop(adj[node]))
            res.append(node)

        dfs("JFK")
        return res[::-1]
