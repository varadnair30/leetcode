
import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        pref = [1] * n
        suff=[1]*n

        # First pass: prefix product
        pref[0]=1
        for i in range(1,n):
            
            pref[i]=pref[i-1]*nums[i-1]
            
        # Second pass: suffix product
        
        suff[-1] = 1
        for i in range(n - 2, -1, -1):
            
            suff[i]=(suff[i+1]*nums[i+1])

        return [pref[i]*suff[i] for i in range(n)]
            
            


        