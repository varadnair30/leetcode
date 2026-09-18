import math
class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:


        #[1,2,3,4,5,6,7,8,9]

        # l               h
        #         m

        if len(nums) > threshold:
            return -1
        maxi=max(nums)
        sumi=0

        low,high=1,maxi

        while low<=high:

            mid=(low+high)//2
            sumi=0
            for i in range(len(nums)):

                sumi+= math.ceil(nums[i]/mid)

            if sumi<=threshold:

                
                high=mid-1

            else:
                low=mid+1

        return low









          












        