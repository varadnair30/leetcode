class Solution:
    def isPalindrome(self, s: str) -> bool:

        s=s.strip().lower()

        if len(s)==0:
            return True

        s_list=list(s)

        left,right=0,len(s)-1

        while left<right:
            if not (s_list[left].isalnum()):
                left+=1
                continue
            if not (s_list[right].isalnum()):
                right-=1
                continue

            if s_list[left]!=s_list[right]:

                return False

            left+=1
            right-=1
        return True
        