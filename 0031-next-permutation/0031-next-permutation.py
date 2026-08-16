class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        index=-1
        # set the dip point
        for i in range(len(nums)-2,-1,-1):

            if nums[i]<nums[i+1]:
                index=i
                break

        # if no dip point found
        if index==-1:
            nums.reverse()
            return

        # find just greater element
        # loop till dip point & find just only next element greater
        for i in range(len(nums)-1,index,-1):

            if nums[i]>nums[index]:

                nums[i], nums[index] = nums[index], nums[i]

                break

        nums[index+1 :] = reversed(nums[index+1:])




        """
        Do not return anything, modify nums in-place instead.
        """


        