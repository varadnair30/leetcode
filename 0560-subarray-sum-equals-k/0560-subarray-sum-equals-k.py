from collections import defaultdict
class Solution:
    def subarraySum(self, arr: List[int], k: int) -> int:

        n=len(arr)
        preSum=cnt=0
        mpp=defaultdict(int)
        mpp[0]=1

        for i in range(n):

            preSum+=arr[i]

            rem=preSum-k
            cnt= cnt+mpp[rem]

            mpp[preSum]+=1

        return cnt

        

        
        