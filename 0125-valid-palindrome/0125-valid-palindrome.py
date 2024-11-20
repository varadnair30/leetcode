class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s=s.lower()
        ch=''
        for i in range(len(s)):
            if s[i].isalnum():
                ch+=s[i]
        
        return (ch[:]==ch[::-1])
                
            
        
    
        
        
        