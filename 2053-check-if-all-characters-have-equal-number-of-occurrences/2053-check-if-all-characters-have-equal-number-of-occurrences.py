from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        lst=list(s)
        

        hash_s=[0]*26
        for i in range(len(lst)):
            hash_s[ord(lst[i]) - 97] += 1 

        for i in range((len(lst)-1)):

            if hash_s[ord(lst[i]) - 97] != hash_s[ord(lst[i+1]) - 97]:
                return False

        return True




        