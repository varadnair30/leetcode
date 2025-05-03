class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        res=[]

        temp1=[nums[i] for i in range(n)]
        temp2=[nums[i] for i in range(n,2*n)]

        for i in range(n):

            res.append(temp1[i])
            res.append(temp2[i])

        return res











        