class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        # traverse from left and see if any elem on right is greater
        # if it is greater then fill the res [i] with that value as nums[i]
        # else loop traverse through the array, once it is traversed completely reverse traversal by i-n and 
        # then if it reaches the same element, break out of loop
        # this is O(N^2)

        n=len(nums)

        nge = [-1] * n

        

        stk=[]

        for i in range(2*n-1,-1,-1):

            while stk and stk[-1]<=nums[i%n]:
                stk.pop()

            if i < n:
                nge[i]= -1 if not stk else stk[-1]

            stk.append(nums[i%n])
        return nge


        






        