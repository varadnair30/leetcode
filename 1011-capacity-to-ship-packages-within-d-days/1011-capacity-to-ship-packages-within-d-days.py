class Solution:
    def func(self,wt, cap):

        days,load=1,0

        for i in range(len(wt)):

            if load+wt[i] > cap:
                days=days+1
                load=wt[i]

            else:
                load+= wt[i]

        return days
    
    def shipWithinDays(self, weights: list[int], days: int) -> int:

        low,high=max(weights), sum(weights)

        while low<=high:

            mid=(low+high)//2
            noOfDays=self.func(weights,mid)
            if noOfDays<=days:

                high=mid-1

            else:
                low=mid+1

        return low










        