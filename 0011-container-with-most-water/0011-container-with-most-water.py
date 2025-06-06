class Solution:
    def maxArea(self, height: List[int]) -> int:

        n=len(height)
        left,right=0,n-1
        res=0
        while left<right:
            area=min(height[left],height[right]) * (right-left)
            res=max(res,area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1

        return res



        