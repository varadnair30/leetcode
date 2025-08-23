class Solution:
    def minWindow(self, s: str, t: str) -> str:


        hash=[0]*256

        l,r=0,0

        minLen=float('inf')
        sIndex=-1
        n,m=len(s),len(t)
        cnt=0

        for i in range(m):

            hash[ord(t[i])]+=1

        for r in range(n):

            if hash[ord(s[r])]>0: cnt+=1

            hash[ord(s[r])]-=1
            
            while cnt==m:

                if r-l+1 < minLen:
                    minLen=r-l+1

                    sIndex=l

                hash[ord(s[l])]+=1

                if (hash[ord(s[l])]>0): cnt-=1

                l+=1
        
        return "" if (sIndex==-1) else s[sIndex:sIndex+minLen]

        

        
        