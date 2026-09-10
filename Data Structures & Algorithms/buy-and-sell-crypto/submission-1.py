class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(len(prices)-1):
            profit=0
            j = i+1
            while j < len(prices):
                profit = prices[j] - prices[i]
                maxProfit = max(maxProfit,profit)
                j = j+1
        return maxProfit