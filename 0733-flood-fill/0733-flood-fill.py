class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        ROWS,COLS = len(image),len(image[0])

        c_image=image
        org_color=c_image[sr][sc]

        if color==org_color: return c_image
        def dfs(r,c):

            if (r<0 or r>=ROWS or c<0 or c>=COLS) or (c_image[r][c]!=org_color):
                return

            
            if c_image[r][c]==org_color:

                c_image[r][c] = color

            dfs(r-1,c)
            dfs(r+1,c)
            
            dfs(r,c-1)
            dfs(r,c+1)
            

        
        dfs(sr,sc)

        return c_image




        
        