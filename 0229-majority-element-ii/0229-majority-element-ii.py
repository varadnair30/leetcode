from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums: return []
        res=[]
        counter=Counter(nums)

        for num, count in counter.items():

            if count> (len(nums) // 3):
                res.append(num)

        return res

        
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        # Dictionary to store the frequency of each element
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        res = []
        n = len(nums)
        for num, count in counts.items():
            if count > (n // 3):
                res.append(num)

        return res

    '''

        




        