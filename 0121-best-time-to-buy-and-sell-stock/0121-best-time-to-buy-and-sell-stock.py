class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit,minProfit=0,float('inf')

        for i in range(len(prices)):

            minProfit=min(minProfit,prices[i])
            maxProfit=max(maxProfit,prices[i]-minProfit)

        return maxProfit


        