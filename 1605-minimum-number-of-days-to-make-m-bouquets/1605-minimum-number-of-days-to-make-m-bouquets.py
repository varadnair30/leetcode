class Solution:
    
    def possible(self,arr,day,m,k):
        n=len(arr)
        cnt=noOfB=0
        for i in range(n):
            if arr[i]<=day:
                cnt+=1
            else:
                noOfB+=cnt//k
                cnt=0
        noOfB+=cnt//k
        return noOfB>=m

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        if len(bloomDay)<(m*k):
            return -1

        mini=min(bloomDay)
        maxi=max(bloomDay)

        low,high=mini,maxi

        while low<=high:
            mid=(low+high)//2
            if(self.possible(bloomDay,mid,m,k)==True):
                high=mid-1
            else:
                low=mid+1
        return low
        

        

        