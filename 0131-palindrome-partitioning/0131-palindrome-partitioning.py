class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res=[]
        path=[]
        def isPalindrome(s,start,end):

            while start<=end:
                if s[start]!=s[end]: return False

                start+=1
                end-=1

            return True
        def func(index):

            if index==len(s):
                res.append(path[:])
                return
            for i in range(index,len(s)):

                if isPalindrome(s,index,i):
                    path.append(s[index:i+1])

                    func(i+1)

                    path.pop()


        func(0)

        return res





        













         

        


        