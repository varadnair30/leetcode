class Solution:
    def shipWithinDays(self, weights: List[int], d: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = (low + high) // 2
            numberOfDays = self.findDays(weights, mid)
            if numberOfDays <= d:
                # Eliminate right half
                high = mid - 1
            else:
                # Eliminate left half
                low = mid + 1
        return low

    def findDays(self,weights, cap):
        days = 1  # First day
        load = 0
        n = len(weights)  # Size of array
        for i in range(n):
            if load + weights[i] > cap:
                days += 1  # Move to next day
                load = weights[i]  # Load the weight
            else:
                # Load the weight on the same day
                load += weights[i]
        return days


    

        
        