class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        start=end=-1

        low,high=0,len(nums)-1

        while low<=high:

            mid=(low+high)//2

            if nums[mid]==target:
                start=mid
                high=mid-1

            elif nums[mid]<target:
                low=mid+1

            else:
                high=mid-1

        
        low,high=0,len(nums)-1

        while low<=high:

            mid=(low+high)//2

            if nums[mid]==target:
                end=mid
                low=mid+1

            elif nums[mid]<target:
                low=mid+1

            else:
                high=mid-1
        

        return [start,end]



        









        