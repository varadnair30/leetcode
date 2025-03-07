class Solution:
    def romanToInt(self, s: str) -> int:

        rToi = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        temp = s[::-1]  
        ans = rToi[temp[0]]  
        
        for i in range(1, len(s)):  
            if rToi[temp[i]] < rToi[temp[i - 1]]:  
                ans -= rToi[temp[i]]
            else:
                ans += rToi[temp[i]]
        
        return ans

        
        