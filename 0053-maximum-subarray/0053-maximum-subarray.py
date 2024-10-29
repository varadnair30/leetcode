class Solution(object):
    def maxSubArray(self, nums):

        resSum=0
        maxi=float('-inf')
        for i in range(len(nums)):
            resSum+=nums[i]

            maxi=max(maxi,resSum)

            if resSum<0:
                resSum=0
        return maxi

        
        """
        :type nums: List[int]
        :rtype: int
        """
        