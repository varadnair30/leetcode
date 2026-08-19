from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        cn1=cn2=0
        elem1=elem2=float('-inf')
        n=len(nums)
        for i in range(n):

            if cn1==0 and elem2!=nums[i]:
                cn1=1
                elem1=nums[i]

            elif cn2==0 and elem1!=nums[i]:
                cn2=1
                elem2=nums[i]

            elif nums[i]==elem1:
                cn1+=1
            elif nums[i]==elem2:
                cn2+=1

            else:
                cn1-=1
                cn2-=1

        ls=[]
        cnt1,cnt2=0,0
        
        for i in range(n):
            if(elem1==nums[i]):
                cnt1+=1
            if(elem2==nums[i]):
                cnt2+=1
                
        mini=(n//3) + 1
        if(cnt1>=mini):
            ls.append(elem1)
        if(cnt2>=mini):
            ls.append(elem2)
        # ls.sort()
        return ls
            
            



        