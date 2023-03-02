class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        dp = [nums[0]]
        for i in range(1,len(nums)):
            a = max(dp[i-1] + nums[i], nums[i])
            dp.append(a)
        print(dp)
        return max(dp)
