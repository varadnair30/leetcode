class Solution:
    def maxDepth(self, s: str) -> int:

        stack=[]
        ans=0
        for i in range(len(s)):
            if s[i]=='(':


                stack.append(s[i])
                ans=max(len(stack),ans)
            elif s[i]==')':
                stack.pop()
            else:
                continue

        return ans
            

        