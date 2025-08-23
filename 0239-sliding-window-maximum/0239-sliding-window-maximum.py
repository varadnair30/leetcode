from collections import deque
class Solution:

    
    
    def maxSlidingWindow(self, a: List[int], k: int) -> List[int]:

        n = len(a)
        r = []
        q = deque()  # store indices

        for i in range(n):
            # remove indices that are out of current window
            if q and q[0] == i - k:
                q.popleft()

            # remove smaller numbers in range k (they’re useless)
            while q and a[q[-1]] < a[i]:
                q.pop()

            # add current index
            q.append(i)

            # once we have at least k elements processed
            if i >= k - 1:
                r.append(a[q[0]])  # front of deque is max in window

        return r





        