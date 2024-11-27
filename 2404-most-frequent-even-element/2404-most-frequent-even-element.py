from collections import Counter
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        
        counter=Counter(nums)
        maxC=-1
        ev=-1
        for nums,count in counter.items():
            if nums%2==0:
                if maxC<count or (count == maxC and nums < ev):
                    maxC=count
                    ev=nums
                    
        return ev
                
                
                
                
                

        
    
        
        
        
        
        