class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nge={}

        stk=[]

        for num in nums2:

            while stk and num > stk[-1]:
                prev_num=stk.pop()
                nge[prev_num]=num
            stk.append(num)

        while stk:
            prev_num=stk.pop()
            nge[prev_num]=-1

        return [nge[num] for num in nums1]






        




        