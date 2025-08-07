class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxi=float('-inf')

        cur_sum=0

        for i in range(len(nums)):

            cur_sum+=nums[i]

            maxi=max(cur_sum,maxi)

            if cur_sum<0: cur_sum=0

        return maxi


        