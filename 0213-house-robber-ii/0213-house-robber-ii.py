class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * (len(nums) - 1)
        dp2 = [-1] * (len(nums) - 1)

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        if len(nums) == 3:
            return max(nums)

        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[2] + dp[0]

        dp2[0] = nums[1]
        dp2[1] = nums[2]
        dp2[2] = nums[3] + dp2[0]

        for i in range(3, len(nums)-1):
            dp[i] = nums[i] + max(dp[i-2], dp[i-3])
            dp2[i] = nums[i+1] + max(dp2[i-2], dp2[i-3])
        
        dp.extend(dp2)
        return max(dp)
