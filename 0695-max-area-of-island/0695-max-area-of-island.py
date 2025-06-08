from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        maxIsland = 0

        def bfs(r, c):
            q = deque()
            visit.add((r, c))
            q.append((r, c))
            cnt = 0
            while q:
                row, col = q.popleft()
                cnt += 1  # increment for each cell visited
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (
                        0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] == 1 and
                        (nr, nc) not in visit
                    ):
                        q.append((nr, nc))
                        visit.add((nr, nc))
            return cnt

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    maxIsland = max(maxIsland, bfs(r, c))

        return maxIsland
