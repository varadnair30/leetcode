class Solution:
    def rearrangeArray(self, A: List[int]) -> List[int]:
        n = len(A)
    
       
        ans = [0] * n
        
        
        posIndex, negIndex = 0, 1
        for i in range(n):
            
        
            if A[i] < 0:
                ans[negIndex] = A[i]
                negIndex += 2
            
        
            else:
                ans[posIndex] = A[i]
                posIndex += 2
        
        return ans






        