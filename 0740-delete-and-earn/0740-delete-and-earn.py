class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        vals = [i for i in range(min(nums), max(nums)+1)]
        scores = [nums.count(i) * i for i in set(vals)]


        if len(vals) == 1:
            return scores[0]
        
        if len(vals) == 2:
            if vals[1] - vals[0] > 1:
                return sum(scores)
            else:
                return max(scores[0], scores[1])
        
        if len(vals) == 3:
            return max(scores[0] + scores[2], scores[1])
        
        dp = [-1] * len(vals)

        dp[0] = scores[0]
        dp[1] = scores[1]
        dp[2] = scores[2] + scores[0]

        for i in range(3, len(vals)):
            dp[i] = scores[i] + max(dp[i-2], dp[i-3])
        
        
        return max(dp)