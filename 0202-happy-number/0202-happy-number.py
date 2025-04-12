class Solution:
    def isHappy(self, n: int) -> bool:

        num=0
        
        mpp=defaultdict(int)
        while True:
            sum=0
            while n!=0:
                sum+= (n%10)**2
                n=n//10

            if sum==1:
                return True
            
            n=sum

            if n in mpp:
                return False

            mpp[n]+=1
            
    






        
        