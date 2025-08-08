class Solution:
    
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLS=len(matrix),len(matrix[0])

        top,bot=0,ROWS-1
        while top<=bot:

            row=(top+bot)//2

            if target>matrix[row][-1]:
                top=row+1

            elif target<matrix[row][0]:
                bot=row-1

            else:

                break
        if (top>bot):
            return False

        row=(top+bot)//2

        low,high=0,COLS-1

        while low<=high:

            mid=(low+high)//2

            if target>matrix[row][mid]:

                low=mid+1

            elif target<matrix[row][mid]:

                high=mid-1

            else:

                return True

        return False



















        