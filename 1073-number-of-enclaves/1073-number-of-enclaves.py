class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:


        '''
        do the dfs and capture the boundary and assign it with 2


        count the 1s which are not connected and assign them as 3

        finally , do the traversal and count the no of 3


        '''


        ROWS,COLS = len(grid),len(grid[0])

        def dfs(r,c):
            if (r<0 or r>=ROWS or c<0 or c>=COLS) or grid[r][c]!=1:
                return

            grid[r][c]=2

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(ROWS):
            for c in range(COLS):

                if((r==0) or r==ROWS-1 or c==0 or c==COLS-1) and grid[r][c]==1:
                    dfs(r,c) #leave the border and its adjacent 1s , convert them to 2
        res=0
        for r in range(ROWS):
            for c in range(COLS):
                if (((r>0) or r<ROWS-1 or c>0 or c<COLS-1) and grid[r][c]==1):
                    res+=1


        return res


                    


        



        





        