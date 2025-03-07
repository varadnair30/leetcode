from collections import Counter, defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:

        mpp=Counter(s)
        buckets= defaultdict(list)
        for char, cnt in mpp.items():
            buckets[cnt].append(char)

        res=[]

        for i in range(len(s),0,-1):

            for c in buckets[i]:
                
                res.append(c*i)
        return ''.join(res)


        

        

        


        