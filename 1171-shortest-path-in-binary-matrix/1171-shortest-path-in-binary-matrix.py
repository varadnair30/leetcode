class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        n = len(grid)
        # If start or end is blocked, return -1
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1

        # 8 directions (including diagonals)
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), 
                      (1, -1), (1, 0), (1, 1)]
        
        # Distance matrix
        dist = [[float('inf')] * n for _ in range(n)]
        dist[0][0] = 1  # Start cell counts as 1 step

        q = deque()
        q.append((0, 0))

        while q:
            r, c = q.popleft()
            # If reached destination, return distance
            if (r, c) == (n-1, n-1):
                return dist[r][c]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Check boundaries and cell open
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    if dist[r][c] + 1 < dist[nr][nc]:
                        dist[nr][nc] = dist[r][c] + 1
                        q.append((nr, nc))

        # Destination not reachable
        return -1
        