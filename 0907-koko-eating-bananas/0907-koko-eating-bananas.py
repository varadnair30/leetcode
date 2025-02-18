import math
class Solution:
    
    def func(self,piles,h):
        totalHours=0
        for i in range(len(piles)):
            totalHours+=math.ceil(piles[i]/h)
        return totalHours
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low,high=1,max(piles)

        while low<=high:
            mid=(low+high)//2
            if self.func(piles,mid) <= h:
                high=mid-1

            else:
                low=mid+1

        return low

        





        