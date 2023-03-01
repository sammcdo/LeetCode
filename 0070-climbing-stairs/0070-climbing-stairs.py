class Solution:
    def climbStairs(self, n: int) -> int:

        if n < 3:
            return n

        memo = [0 for x in range(n + 1)]

        memo[0] = 0
        memo[1] = 1
        memo[2] = 2

        for x in range(3, n + 1):
            memo[x] = memo[x-1] + memo[x-2]
        
        return memo[-1]