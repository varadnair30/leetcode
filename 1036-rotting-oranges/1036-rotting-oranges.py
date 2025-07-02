from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        if not grid: return 0

        # Do bfs traversal if current orange is rotten (2) , then explore in nearby directions and see if there is fresh orange(1), store them in queue and convert them to 2. Everytime done with this process, do iteration++ variable
        # do not need set because we are making changes in the grid itself
        # store directions
        
        ROWS,COLS= len(grid),len(grid[0])

        
        q=deque()
        time=fresh=0
        
        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c]==1:
                    fresh+=1
            
                if grid[r][c]==2:
                    q.append((r,c))
        
        directions=[[1,0],[-1,0],[0,1],[0,-1]]

        while q and fresh>0:
            for i in range(len(q)):
                r,c=q.popleft()

                for dr,dc in directions:
                    nr,nc = dr+r,dc+c

                    if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc]==1:
                        

                        grid[nr][nc]=2

                        q.append((nr,nc))

                        fresh-=1
            time+=1
        return time if fresh==0 else -1

        
            





        