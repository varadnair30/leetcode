class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j=1,1
        while i < len(nums):
            if nums[i]!=nums[i-1]:
                nums[j]=nums[i]
                j+=1
            i+=1
            
        return j

                


        
        