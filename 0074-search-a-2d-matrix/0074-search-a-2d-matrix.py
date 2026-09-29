class Solution:
    def searchMatrix(self, mat: list[list[int]], target: int) -> bool:


        if not mat: return False


        rows,cols=len(mat),len(mat[0])

        low,high=0,(rows*cols)-1

        while low<=high:


            mid=(low+high)//2

            if mat[mid//cols][mid%cols]==target:
                return True

            elif mat[mid//cols][mid%cols]<target:
                low=mid+1
            else:
                high=mid-1

        return False

            



        






        