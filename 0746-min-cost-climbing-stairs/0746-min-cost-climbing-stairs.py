class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)

        dp[0] = cost[0]
        dp[1] = cost[1]

        i = 2
        while i < len(dp):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
            i += 1

        return min(dp[-1], dp[-2])
