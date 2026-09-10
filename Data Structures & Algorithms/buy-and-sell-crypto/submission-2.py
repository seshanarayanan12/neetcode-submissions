class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        bP = prices[0]
        for i in prices:
            maxProfit = max(maxProfit, i - bP)
            bP = min(bP,i)
        return maxProfit