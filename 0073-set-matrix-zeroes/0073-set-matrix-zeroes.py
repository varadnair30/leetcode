class Solution:
    
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m=len(matrix)
        n=len(matrix[0])

        row= [0]* m
        col= [0]* n

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row[i]=1

                    col[j]=1

        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j]=0


                


    
         

        





        """
        Do not return anything, modify matrix in-place instead.
        """
        