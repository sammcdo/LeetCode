class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = []

        if n == 0:
            return [0]
        if n == 1:
            return [0,1]

        dp.append(0)
        dp.append(1)
        x = 1
        for i in range(2, n+1):
            if i == 2**(x+1):
                x += 1
            dp.append(1 + dp[i-(2**x)])
        
        return dp