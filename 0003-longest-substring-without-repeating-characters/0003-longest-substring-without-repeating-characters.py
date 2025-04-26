class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hash=[-1]*256
        n=len(s)
        l=r=maxlen=0
        while r<n:
            if hash[ord(s[r])]!=-1:

                if hash[ord(s[r])]>=l:

                    l=hash[ord(s[r])]+1

            maxlen=max(maxlen,r-l+1)
            hash[ord(s[r])]=r
            r+=1

        return maxlen
        