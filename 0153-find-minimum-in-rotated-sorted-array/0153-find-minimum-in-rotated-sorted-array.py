class Solution:
    def findMin(self, arr: List[int]) -> int:

        low,high=0,len(arr)-1
        ans=float('inf')
        while low<=high:
            mid=(low+high)//2
            if arr[low]<=arr[mid]:
                ans=min(ans,arr[low])
                low=mid+1

            else:
                high=mid-1
                ans=min(ans,arr[mid])

        return ans

        
        