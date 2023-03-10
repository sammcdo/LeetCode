class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [-1 for i in range(n+1)]

        if n == 0:
            return [0]
        if n == 1:
            return [0,1]

        dp[0] = 0
        dp[1] = 1
        x = 1
        for i in range(2, n+1):
            if i == 2**(x+1):
                x += 1
            dp[i] = 1 + dp[i-(2**x)]
        
        return dp