class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        low,high=0,n-1
        
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                low=mid+1
            else:
                high=mid-1
                
        return -1
        
        '''
        # recursive approach just uncomment the block '
        
        def binarySearch(self, nums, low, high, target):
            
            if low>high:
                return -1
            
            mid = (low+high)//2
            
            if nums[mid]==target:
                return mid
            elif target > nums[mid]:
                return binarySearch(self,nums,mid+1,high,target)
            
            return binarySearch(self,nums,low,mid-1,target)
        
        return binarySearch(self,nums,0,len(nums)-1,target)
            
    '''
        
        