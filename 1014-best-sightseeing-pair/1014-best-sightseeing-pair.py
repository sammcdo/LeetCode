class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        if len(values) == 2:
            return values[0]+values[1] - 1
        
        dp = [-1] * len(values)
        
        dp[0] = 0
        dp[1] = values[0]+values[1] - 1
        
        prevMax = max(values[0], values[1])
        prevMaxLoc = values.index(prevMax)
        m = dp[1]
        for i in range(2, len(values)):
            if prevMax + values[i] - i + prevMaxLoc >= m:
                m = prevMax + values[i] - i + prevMaxLoc
            
            if values[i] >= prevMax - i + prevMaxLoc:
                prevMax = values[i]
                prevMaxLoc = i
        
        return m
            