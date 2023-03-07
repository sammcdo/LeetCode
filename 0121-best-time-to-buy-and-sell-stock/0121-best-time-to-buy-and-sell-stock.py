class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        if len(prices) == 2:
            if prices[0] <= prices[1]:
                return prices[1] - prices[0]
            else:
                return 0
        
        h = None
        l = None
        m = 0
        for i in range(0, len(prices)):
            if l == None:
                l = prices[i]
            elif h == None:
                if prices[i] >= l:
                    h = prices[i]
                if prices[i] < l:
                    l = prices[i]
                    h = prices[i]
                if h-l > m:
                    m = h-l
            else:
                if prices[i] < l:
                    l = prices[i]
                    h = prices[i]
                if prices[i] > h:
                    h = prices[i]
                if h-l > m:
                    m = h-l
        return m