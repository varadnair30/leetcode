class Solution:
    def longestConsecutive(self, a: List[int]) -> int:
        n=len(a)
        if n==0:
            return 0
        st=set()

        longest=1

        for i in range(n):
            st.add(a[i])

        for item in st:
            if item - 1 not in st:
                cnt=1
                x=item
                while x + 1 in st:
                    x+=1
                    cnt+=1
                longest=max(longest,cnt)
        return longest

        




        '''a.sort()
        curCnt=0
        lastSmaller=float('-inf')
        longest=0

        for i in range(len(a)):
            if (a[i]-1 == lastSmaller):
                curCnt+=1
                lastSmaller=a[i]
            
            elif (a[i]!=lastSmaller):

                curCnt=1
                lastSmaller=a[i]

            longest=max(longest,curCnt) 
        return longest
        '''

