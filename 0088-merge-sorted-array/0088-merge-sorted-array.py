class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        if len(nums1)==0:
            nums1.append(nums2.sort())
        
        else:
            for i in range(n):
                nums1[m+i]=nums2[i]
            
            nums1=nums1.sort()
        
        """
        Do not return anything, modify nums1 in-place instead.
        """
        