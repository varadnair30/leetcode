class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        n=len(nums)
        ans=float('-inf')
        pref=suff=1
        for i in range(n):
            if pref==0:
                pref=1
            if suff==0:
                suff=1
            pref*=nums[i]
            suff*=nums[n-i-1]
            ans=max(ans,max(pref,suff))
        return ans


        

        