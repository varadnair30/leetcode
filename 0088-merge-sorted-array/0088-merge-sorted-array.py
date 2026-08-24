class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        '''
        - check if nums1<nums 2 , return []
        - run a loop from m to m+n
        - put nums2 items in nums1
        - sort the nums1 array
        
        '''

        #m,n=len(nums1),len(nums2)

        
        # nums1=[1,2,3,0,0]
        # nums2 = [2,5]
        
        for i in range(m,m+n):
                nums1[i]=nums2[i-m] # nums2[3-2]

        
        nums1.sort()
