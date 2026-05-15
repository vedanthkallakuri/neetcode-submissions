class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lowestLeft = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[i] - lowestLeft)
            lowestLeft = min(lowestLeft, prices[i])
        return maxProfit