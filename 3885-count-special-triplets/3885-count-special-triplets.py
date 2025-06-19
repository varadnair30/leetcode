from collections import Counter

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        left = Counter()
        right = Counter(nums)
        count = 0

        MOD= 10**9 + 7
        for j in range(len(nums)):
            right[nums[j]] -= 1
            target = nums[j] * 2
            count += left[target] * right[target]
            left[nums[j]] += 1
        return count%MOD



        
        