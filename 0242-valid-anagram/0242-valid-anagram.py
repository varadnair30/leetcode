class Solution:
    def isAnagram(self, s1: str, s2: str) -> bool:

        n1=len(s1)
        n2=len(s2)
        if n1!=n2:
            return False

        
        counts_s1=[0]*26
        counts_s2=[0]*26

        for i in range(n1):
            counts_s1[ord(s1[i])-97]+=1
            counts_s2[ord(s2[i])-97]+=1

        
        
            
        return counts_s1==counts_s2


        



        
        