class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        mpp_s_t={}
        mpp_t_s={}

        for i in range(len(s)):
            if s[i] in mpp_s_t and mpp_s_t[s[i]]!=t[i]:
                return False
            if t[i] in mpp_t_s and mpp_t_s[t[i]]!=s[i]:
                return False
            mpp_s_t[s[i]]=t[i]
            mpp_t_s[t[i]]=s[i]
        return True





















        