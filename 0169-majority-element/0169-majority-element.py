class Solution:
    def majorityElement(self, arr: List[int]) -> int:
        count,ret=0,0
        for i in arr:
            if count==0:
                ret=i
            if i!=ret:
                count-=1
            else:
                count+=1
        return ret




        

        