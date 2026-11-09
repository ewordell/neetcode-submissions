class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(0, len(prices) - 1):
            for j in range(i, len(prices)):
                max_profit = max(prices[j] - prices[i], max_profit)
             
        return max_profit