class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        breakPointIndex = -1
        n=len(nums)
        for i in range(n-2,-1,-1):
            if(nums[i] < nums[i+1]):
                breakPointIndex = i
                break
        

        if breakPointIndex == -1:
            nums[:] = nums[::-1]
        else:
            for i in range(n-1,breakPointIndex,-1):
                
                if nums[i] > nums[breakPointIndex]:
                    nums[breakPointIndex],nums[i]=nums[i],nums[breakPointIndex]
                    break

            nums[breakPointIndex + 1:]=nums[breakPointIndex + 1:][::-1]


        
        
        """
        Do not return anything, modify nums in-place instead.
        """
        