class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort()
        s.sort()

        n,m=len(g),len(s)

        l=r=0

        while l<m and r<n: #Might happen that children are very less in number , so r might reach the end faster

            if g[r]<=s[l]:

                r+=1

            l+=1

        return r
        