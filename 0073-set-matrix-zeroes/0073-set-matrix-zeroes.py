class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        row,col=len(matrix),len(matrix[0])
        row_ar,col_ar=[0]*row, [0]*col

        for i in range(row):
            for j in range(col):

                if matrix[i][j]==0:
                    row_ar[i]=1
                    col_ar[j]=1

        for i in range(row):
            for j in range(col):
                if (row_ar[i]==1 or col_ar[j]==1):
                    matrix[i][j]=0

        



        """
        Do not return anything, modify matrix in-place instead.
        """
        