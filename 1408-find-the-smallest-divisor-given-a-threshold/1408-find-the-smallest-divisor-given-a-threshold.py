import math
class Solution:
    def divSum(self,nums,no):
        n=len(nums)
        sumi=0
        for items in nums:
            sumi+=math.ceil(items/no)

        return sumi

    
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        
        n=len(nums)
        if n>threshold:
            return -1
        
        low,high=1,max(nums)
        

        while low<=high:
            mid=(low+high)//2

            if (self.divSum(nums,mid)<=threshold):
                
                high=mid-1
                
                

            else:
                low=mid+1
        return low
                




        