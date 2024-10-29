class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mProfit,minPrice=0,float('inf')

        for i in range(len(prices)):
            minPrice=min(minPrice,prices[i])
            mProfit=max(mProfit,prices[i]-minPrice)

        return mProfit








        