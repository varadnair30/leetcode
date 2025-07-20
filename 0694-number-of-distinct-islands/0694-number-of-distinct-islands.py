class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        vis = [[0] * n for _ in range(m)]

        def dfs(r,c,base_r,base_c,shapeArr):
            vis[r][c]=1
            shapeArr.append((r-base_r,c-base_c)) #Normalizing the shape and storing it in shapeArr []
            directions=[(1,0),(-1,0),(0,1),(0,-1)]
            for dr,dc in directions:

                nr,nc = dr+r, dc+c
                
                if 0<=nr<m and 0<=nc<n and not vis[nr][nc] and grid[nr][nc]==1:
                    dfs(nr,nc,base_r,base_c,shapeArr)

        shapes=set()

        for i in range(m):
            for j in range(n):

                if grid[i][j]==1 and not vis[i][j]:
                    storeShape=[]
                    dfs(i,j,i,j,storeShape)
                    # Converting relative coordinates to string for hashable comparison

                    parts = []

                    
                    for x, y in storeShape:
                    
                        parts.append(str(x) + "_" + str(y))

                    
                    shape_str = ",".join(parts)

                    shapes.add(shape_str)

        return len(shapes)



        