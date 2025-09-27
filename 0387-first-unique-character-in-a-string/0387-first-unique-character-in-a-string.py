from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:

        mpp=Counter(s)

        for i in range(len(s)):

            if mpp[s[i]]==1: return i


        return -1


        