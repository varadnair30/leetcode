class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n=len(nums)
        if n <=1: return []
        mpp={}
        preSum=0
        for i in range(n):

            if target-nums[i] in mpp:
                return [mpp[target-nums[i]],i]


            mpp[nums[i]]=i


