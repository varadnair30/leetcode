class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        count1=count2=count0=0
        n=len(nums)
        for i in range(n):

            if nums[i]==0:
                count0+=1
            elif nums[i]==1:
                count1+=1

            else:
                count2+=1

        for x in range(count0):
            nums[x]=0
        for x in range(count0,count0+count1):
            nums[x]=1

        for x in range(count0+count1,count0+count1+count2):
            nums[x]=2
        
