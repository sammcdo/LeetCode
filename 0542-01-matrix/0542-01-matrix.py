class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dp = []
        queue = []

        high = max(len(mat), len(mat[0]))

        for i in range(len(mat)):
            dp.append([])
            for j in range(len(mat[0])):
                dp[-1].append(high)
                if mat[i][j] == 0:
                    dp[i][j] = 0
                    queue.append([i,j])
        
        newCoords = [[1, 0],[0,1],[-1,0],[0,-1]]
        while len(queue) > 0:
            i, j = queue.pop(0)
            for l,m in newCoords:
                if i+l >= 0 and i+l <= len(mat)-1:
                    if j+m >= 0 and j+m <= len(mat[0])-1:
                        if dp[i+l][j+m] > dp[i][j] + 1:
                            dp[i+l][j+m] = dp[i][j] + 1
                            queue.append([i+l,j+m])

        return dp

