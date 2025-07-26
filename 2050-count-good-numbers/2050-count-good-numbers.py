class Solution:
     
    def findPower(self,a,b):
        MOD= (10**9)+7

        if b==0: return 1

        half=self.findPower(a,b//2)
        result = (half*half) % MOD

        if b&1==1: result=(result*a)%MOD

        return result
    
    def countGoodNumbers(self, n: int) -> int:
        MOD= (10**9)+7
        return self.findPower(5,(n+1)//2) * (self.findPower(4, n//2))% MOD

        




        