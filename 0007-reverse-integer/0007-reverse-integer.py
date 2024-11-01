class Solution:
    def reverse(self, x: int) -> int:
        
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        
        
        is_negative = x < 0
        
        
        x_str = str(abs(x))
        
        
        reversed_x = int(x_str[::-1])
        
        
        if is_negative:
            reversed_x = -reversed_x
        
        
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
        
        return reversed_x
        
        
        
        
        
        