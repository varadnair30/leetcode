from collections import defaultdict
class Solution:
    def beautySum(self, s: str) -> int:

        cur_sum=0
        n=len(s)
        for i in range(n):
            freq= defaultdict(int)
            for j in range(i,n):
                freq[s[j]]+=1

                mi=min(freq.values())
                mx=max(freq.values())

                cur_sum+= mx-mi
        return cur_sum





        