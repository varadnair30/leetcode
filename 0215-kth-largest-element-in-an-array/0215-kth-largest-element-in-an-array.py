import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heapq.heapify(nums)

        n=len(nums)
        cur_list=[0]*n

        for i in range(n):
            minn=heapq.heappop(nums)

            cur_list[i]=minn

        return cur_list[-k]












        
        