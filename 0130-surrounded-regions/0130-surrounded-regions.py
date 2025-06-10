class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # assign nearby '0' are only converted to 'X' only when they are not near the edge 
        # if r is 0 or len_row - 1 or c is 0 or len_col - 1
        ROWS,COLS = len(board),len(board[0])
        

        def dfs(r,c):

            if (r<0 or r>=ROWS or c<0 or c>=COLS or board[r][c]!='O'):
                return

            board[r][c]='#'

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if (r==0 or r==ROWS-1 or c==0 or c==COLS-1) and board[r][c]=='O':
                    dfs(r,c)
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]== 'O':
                    board[r][c] = 'X'

                elif board[r][c]=='#':
                    board[r][c]= 'O'

                


        