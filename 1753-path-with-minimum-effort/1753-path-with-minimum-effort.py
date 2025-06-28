import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:


        n, m = len(heights), len(heights[0])
        
        # Priority queue: (effort_so_far, row, col)
        pq = [(0, 0, 0)]
        
        # Distance matrix: minimal effort to reach cell (i, j) 
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0
        
        # 4 possible directions
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        
        while pq:
            diff, row, col = heapq.heappop(pq)
            
            # If reached destination, return effort
            if row == n-1 and col == m-1:
                return diff
            
            for i in range(4):
                newr, newc = row + dr[i], col + dc[i]
                
                # If valid cell
                if 0 <= newr < n and 0 <= newc < m:
                    # Max effort needed to reach this neighbor
                    newEffort = max(abs(heights[row][col] - heights[newr][newc]), diff)
                    if newEffort < dist[newr][newc]:
                        dist[newr][newc] = newEffort
                        heapq.heappush(pq, (newEffort, newr, newc))
        
        return 0  # If unreachable



        