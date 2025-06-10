from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q=deque()
        time=fresh=0
        ROWS,COLS = len(grid),len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c]== 1:
                    fresh+=1

                if grid[r][c] ==2:
                    q.append([r,c])

        directions=[[1,0],[-1,0],[0,1],[0,-1]]

        while q and fresh>0:
            
            for i in range(len(q)):
                r,c = q.popleft()

                for dr,dc in directions:

                    nr, nc = dr+r, dc+c

                    if nr<0 or nr>=ROWS or nc<0 or nc>=COLS or grid[nr][nc]!=1: # either out of bounds or if grid cell is not a fresh orange

                        continue

                    grid[nr][nc]= 2

                    q.append([nr,nc])

                    fresh-=1
            time+=1

        return time if fresh==0 else -1

            





        


        




            


        # If near '2' , 1s will start rotting 
        # each 1st near 2 will rot in each different iterations

        # return the minimum possible iterations




        
        