from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        '''
        treat k as src 
        tot_time=0
        (src,target,cumulative_time_taken)
        inside while q put tot_time+=cumulative_time_taken
        '''
        adjLst=defaultdict(list)
        for u,v,w in times:

            adjLst[u].append((v,w))


        dist=[float('inf')] * (n+1)

        dist[k]=0

        minHeap=[(0,k)]

        while minHeap:

            time,node = heapq.heappop(minHeap)

            for neighbor, weight in adjLst[node]:
                if time + weight < dist[neighbor]:

                    dist[neighbor]=time + weight

                    heapq.heappush(minHeap,(dist[neighbor],neighbor))

        max_time=max(dist[1:]) #since the nodes are from 1-n

        return max_time if max_time != float('inf') else -1




        minHeap=[(0,k)]
        visit=set()


        








        