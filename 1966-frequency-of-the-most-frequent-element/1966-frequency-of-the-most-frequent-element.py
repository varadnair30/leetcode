class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        nums.sort()

        left=0
        ans=0
        sum=0

        for right in range(len(nums)):
            sum+=nums[right]
            while((right-left+1)*nums[right] > sum+k):
                sum-=nums[left]
                left+=1
            
            ans=max(ans,right-left+1)

        return ans


        