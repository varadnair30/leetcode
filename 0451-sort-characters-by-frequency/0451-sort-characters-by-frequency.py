from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:

        mpp=Counter(s)
        sorted_chars=sorted(mpp.keys(), key=lambda x: -mpp[x])

        return "".join(x * mpp[x] for x in sorted_chars)

        

        


        