class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        xr=0
        for i in range(len(nums)):

            xr^= nums[i]

        return xr 
        