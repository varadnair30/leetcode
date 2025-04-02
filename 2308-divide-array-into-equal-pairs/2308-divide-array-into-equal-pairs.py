
class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        #Using Bit Manipulation where shifting of significant bit can decide where the no. is odd or even
        
        bit_mask = 0  
        for num in nums:
            bit_mask ^= 1 << num  

        return bit_mask == 0

            
        