class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:


        '''
        sort the array
        keep i and j fixed and do the 2 pointer approach using k and l
        run a loop with i and if condition of non same elements & j under that loop (j=i+1)and if condition of non same elements

        while k<l then compute summation of all 4 elems

        if sum=target, append into res array and increase k and decrease l, and inside only check or duplicate elements of k and l

        elif sum<target, k++
        else l--

        '''

        n=len(nums)
        nums.sort()
        sumi=0
        res=[]
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]: continue

            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]: continue

                k=j+1
                l=n-1

                while k<l:

                    sumi= nums[i]+nums[j]+nums[k]+nums[l]

                    if sumi==target:
                        res.append([nums[i],nums[j],nums[k],nums[l]])
                        
                        while k<l and nums[k]==nums[k+1]: k+=1

                        while k<l and nums[l]==nums[l-1]: l-=1

                        k+=1
                        l-=1

                    elif sumi<target: k+=1

                    else: l-=1
        return res




        