class Solution:
    def minAvailableDuration(self, slotsA: List[List[int]], slotsB: List[List[int]], dur: int) -> List[int]:

        slotsA.sort()
        slotsB.sort()
        i=j=0
        while i<len(slotsA) and j<len(slotsB):

            start = max(slotsA[i][0], slotsB[j][0])
            end = min(slotsA[i][1], slotsB[j][1])

            if (end-start >= dur):
                return [start, start + dur]

            if (slotsA[i][1] < slotsB[j][1]):
                i+=1
            else:
                j+=1

        return []
            