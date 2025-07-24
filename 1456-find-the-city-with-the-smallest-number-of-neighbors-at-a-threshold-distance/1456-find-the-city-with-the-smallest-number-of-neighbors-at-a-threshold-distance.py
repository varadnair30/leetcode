class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:



        '''
        n cities , 0 to n-1
        edges=[from,to,weight]

        '''
        INF = float('inf')
        
        # Step 1: Initialize distance matrix
        dist = [[INF for _ in range(n)] for _ in range(n)]
        
        # Step 2: Populate direct distances from edges
        for u, v, wt in edges:
            dist[u][v] = wt
            dist[v][u] = wt
        
        # Step 3: Set diagonal to 0 (distance to self)
        for i in range(n):
            dist[i][i] = 0
        
        # Step 4: Floyd-Warshall algorithm to update shortest paths
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] != INF and dist[k][j] != INF:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        # Step 5: Find the city with minimum reachable cities (with tie-breaker: larger city index)
        min_count = n + 1
        city_no = -1
        
        for city in range(n):
            count = 0
            for neighbor in range(n):
                if dist[city][neighbor] <= distanceThreshold:
                    count += 1
            
            if count <= min_count:
                min_count = count
                city_no = city  # update if fewer or same number but higher index
        
        return city_no
        






        