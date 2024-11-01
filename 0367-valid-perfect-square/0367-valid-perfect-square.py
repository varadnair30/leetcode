class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sum=0
        for i in range(1,num+1,2):
            sum+=i
            if sum==num:
                return True
            elif sum > num:
                break
            
        return False
            
         
        
        