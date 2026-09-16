import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def func(piles,speed):

            totalH=0
            for bananas in piles:
                totalH+= math.ceil(bananas/speed)

            return totalH
        
        low,high=1,max(piles)
        ans=float('inf')
        

        while low<=high:

            mid=(low+high)//2

            totalH= func(piles,mid)

            if totalH<=h:
                ans=mid
                high=mid-1

            else:
                low=mid+1

        return ans






        