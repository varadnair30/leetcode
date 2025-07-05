from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        ROW,COL= len(mat),len(mat[0])

        dist=[[0]* COL for _ in  range(ROW)]
        vis=[[0]* COL for _ in  range(ROW)]

        q=deque()


        #Adding all 0 to queue and marking visited

        for i in range(ROW):
            for j in range(COL):

                if mat[i][j]==0:
                    q.append((i,j,0)) #coordinates and distance , wherever it is 0, distance is 0 as well

                    vis[i][j]=1

        directions=[[1,0],[-1,0],[0,1],[0,-1]]

        while q:

            row, col, steps= q.popleft()

            dist[row][col] = steps

            for dr, dc in directions:

                nr, nc = dr+row , col+dc

                if 0<=nr<ROW and 0<=nc<COL and not vis[nr][nc]:
                    vis[nr][nc] = 1

                    q.append((nr,nc, steps+1))


        return dist 




















        