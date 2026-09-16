class Solution:
    def is_possible(self,bloom_days,day,m,k):

        count=bouquets=0

        for bloom in bloom_days:
            if bloom<=day:
                count+=1
                if count==k:
                    bouquets+=1
                    count=0
            else:
                count=0
        return bouquets>=m

    
    
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        if m*k > len(bloomDay): return -1
        low,high=min(bloomDay),max(bloomDay)
        answer=-1

        while low<=high:

            mid=(low+high)//2
            if self.is_possible(bloomDay,mid,m,k):
                answer=mid
                high=mid-1

            else:
                low=mid+1

        return answer






        