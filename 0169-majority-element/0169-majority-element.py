class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        n=len(nums)
        cnt=el=0

        for num in nums:

            if cnt==0:
                cnt=1
                el=num
            elif el==num:
                cnt+=1
            else:
                cnt-=1

        cnt1=nums.count(el)

        return el if cnt1> (n//2) else -1





        