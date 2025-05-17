from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:


        '''even_elem,odd_elem=[],[] # O(1)
        for i in range(len(s)):
            if s.count(s[i]) %2 ==0: #even freq
                even_elem.append([s.count(s[i]),s[i]])

            else:
                odd_elem.append([s.count(s[i]),s[i]])

        even_elem.sort()
        odd_elem.sort()

        return (odd_elem[-1][0])-(even_elem[0][0])
'''
        even_elem,odd_elem=[],[]
        mpp=Counter(s)
        
        for key,freq in mpp.items():

            if freq % 2 ==0:
                even_elem.append(freq)

            else:
                odd_elem.append(freq)

        return max(odd_elem)-min(even_elem)













        