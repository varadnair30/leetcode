
class Solution:
    

    def checkValid(self, matrix: List[List[int]]) -> bool:
        n=len(matrix)
        expected=set(range(1,n+1))

        for r in matrix:
            if set(r)!=expected:
                return False

            
        for j in range(n):
            col=[matrix[i][j] for i in range(n)]

            if set(col)!=expected:
                return False

        return True

            

        

            
                
        