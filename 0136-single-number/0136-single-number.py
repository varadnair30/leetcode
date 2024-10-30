class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        res=0
        for items in nums:
            res^=items
            
        return res
            
        