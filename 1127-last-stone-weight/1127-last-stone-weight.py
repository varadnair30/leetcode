import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:


        # heapify it array into put into max heap
        # whenever get 0 , do not push into heap
        # when len(heap)==1 then return heapq.pop(stones array)

        
        n=len(stones)
        max_heap=[-num for num in stones]
        heapq.heapify(max_heap)
         
        while len(max_heap) > 1:
            y = -heapq.heappop(max_heap)  # Heaviest
            x = -heapq.heappop(max_heap)  # Next heaviest

            if y != x:
                # Push the difference back, as a negative (for max-heap)
                heapq.heappush(max_heap, -(y - x))

        # If any stone is left, return its weight; otherwise, return 0
        return -heapq.heappop(max_heap) if max_heap else 0



            




        










        