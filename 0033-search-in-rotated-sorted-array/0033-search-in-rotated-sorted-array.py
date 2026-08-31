class Solution:
    def search(self, nums: List[int], target: int) -> int:


        # if target in left half, return that index
        # if in right half , return that index

        low,high=0,len(nums)-1

        while low<=high:

            mid=(low+high)//2

            if nums[mid]==target:
                return mid

            if nums[mid]>=nums[low]:

                if nums[low]<= target and nums[mid]>=target:

                    high=mid-1

                else:
                    low=mid+1

            else:

                if nums[mid]<= target and nums[high]>=target:

                    low=mid+1

                else:
                    high=mid-1



        return -1










        