class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        sumOfTrades = 0
        low = prices[0]
        high = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < high:
                sumOfTrades += high - low
                low = prices[i]
                high = prices[i]
            elif prices[i] > high:
                high = prices[i]
        
        sumOfTrades += high - low

        return sumOfTrades