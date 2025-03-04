class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=''
        strs.sort()
        first=strs[0]
        last=strs[len(strs)-1]

        for i in range(len(first)):
            if first[i]!=last[i]:
                break
            prefix+=first[i]

        return prefix

        










        