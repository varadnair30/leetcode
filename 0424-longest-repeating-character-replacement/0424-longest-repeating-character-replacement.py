from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        n=len(s)
        count=defaultdict(int)

        maxf=l=res=r=0

        while r<n:

            count[s[r]]+=1

            maxf=max(maxf,count[s[r]])

            if((r-l+1)-maxf>k):

                count[s[l]]-=1
                l+=1

            res=max(res,r-l+1)
            r+=1

        return res
        