class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        dumm1=[]
        dumm2=[]
        for i in range(len(nums)):

            if nums[i]>0: dumm1.append(nums[i]) # +ve elements #[,1,2]
            else:
                dumm2.append(nums[i]) # -ve elements #,-5,-4

        res=[]

        for i in range(len(dumm1)):
            res.append(dumm1[i])
            res.append(dumm2[i])

        return res





        