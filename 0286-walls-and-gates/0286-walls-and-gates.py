from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]: return
        INF = 2**31 - 1
        ROWS,COLS = len(rooms),len(rooms[0])

        q=deque()

        for r in range(ROWS):
            for c in range(COLS):

                if rooms[r][c]==0:
                    q.append((r,c))

        directions=[[1,0],[-1,0],[0,1],[0,-1]]

        while q:

            r,c=q.popleft()

            for dr,dc in directions:

                nr,nc=dr+r,dc+c

                if 0<=nr<ROWS and  0<=nc<COLS and rooms[nr][nc]== INF:
                    rooms[nr][nc]=rooms[r][c] + 1

                    q.append((nr,nc))
        