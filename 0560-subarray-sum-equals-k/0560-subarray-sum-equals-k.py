from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        
        mpp=defaultdict(int)
        mpp[0]=1
        preSum,cnt=0,0
        n=len(nums)
        for i in range(n):
            preSum+=nums[i]
            remove=preSum-k
            cnt+=mpp[remove]
            
            mpp[preSum]+=1
            
        return cnt
        