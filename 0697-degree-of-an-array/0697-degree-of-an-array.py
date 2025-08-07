from collections import defaultdict, Counter

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        

        if (len(nums)>50000 and len(nums)<1): return 0

        count, first = defaultdict(int), {}
        degree, ans = 0, len(nums)

        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            count[num] = count[num] + 1

            if count[num] > degree:
                degree = count[num]
                ans = i - first[num] + 1
            elif count[num] == degree:
                ans = min(ans, i - first[num] + 1)

        return ans






        