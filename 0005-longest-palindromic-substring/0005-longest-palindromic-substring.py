class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]

        longest=""
        for i in range(len(s)):
            pal1=expand(i,i)
            pal2=expand(i,i+1)

            longest=max(longest,pal1,pal2, key=len)

        return longest

        

            

        