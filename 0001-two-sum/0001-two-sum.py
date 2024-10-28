class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        resmap={}
        for i in range(len(nums)):
            if (target-nums[i]) in resmap:
                return [resmap[target-nums[i]],i]
            
            resmap[nums[i]]=i



        