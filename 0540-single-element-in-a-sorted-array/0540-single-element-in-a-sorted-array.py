class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        n=len(nums)

        if n==1:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[n-1]!=nums[n-2]:
            return nums[n-1]
        low,high=1,n-2

        while(low<=high):
            mid=(low+high)//2

            if(nums[mid]!=nums[mid+1] and nums[mid]!=nums[mid-1]):
                return nums[mid]
            # left half
            if((mid&1 == 1) and nums[mid-1]==nums[mid]) or ((mid&1 ==0) and nums[mid]==nums[mid+1]):

                low=mid+1 #eliminate left half
            else: #any other case apart from left half , means we are on right half
                high=mid-1 #eliminate right half
        return -1
        
        



        