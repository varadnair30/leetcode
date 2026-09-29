class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:


        if not mat: return False

        n,m=len(mat),len(mat[0])

        row,col=0,m-1

        while row<n and col>=0:

            if mat[row][col]==target: return True

            elif mat[row][col]<target: row+=1

            else:
                col-=1

        return False







        