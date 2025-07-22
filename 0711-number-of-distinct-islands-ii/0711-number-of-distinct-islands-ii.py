class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:

        # only 2 islands
        # 
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]
        shapes = set()

        def dfs(r, c, coords):
            visited[r][c] = True
            coords.append((r, c))
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == 1:
                    dfs(nr, nc, coords)

        def normalize(coords):
            transforms = [[] for _ in range(8)]
            for x, y in coords:
                transforms[0].append(( x,  y))
                transforms[1].append(( x, -y))
                transforms[2].append((-x,  y))
                transforms[3].append((-x, -y))
                transforms[4].append(( y,  x))
                transforms[5].append(( y, -x))
                transforms[6].append((-y,  x))
                transforms[7].append((-y, -x))

            norm_forms = []
            for t in transforms:
                # Normalize: shift all coordinates to start from (0, 0)
                t.sort()
                base_x, base_y = t[0]
                shifted = [(x - base_x, y - base_y) for x, y in t]
                norm_forms.append(tuple(shifted))

            return min(norm_forms)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    coords = []
                    dfs(i, j, coords)
                    shape_key = normalize(coords)
                    shapes.add(shape_key)

        return len(shapes)




        