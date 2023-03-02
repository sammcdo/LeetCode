class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        nums2 = nums + nums

        t = [True if i < 0 else False for i in nums]

        
        if len(nums) == 1:
            return nums[0]
        
        maximum = self.maxSubArray(nums)
        minimum = self.minSubArray(nums)

        if False in t:
            return max(maximum, sum(nums) - minimum)
        else:
            return min(maximum, sum(nums) - minimum)
    
    def minSubArray(self,nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = [nums[0]]
        for i in range(1,len(nums)):
            a = min(dp[i-1] + nums[i], nums[i])
            dp.append(a)
        
        return min(dp)
        
        
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = [nums[0]]
        for i in range(1,len(nums)):
            a = max(dp[i-1] + nums[i], nums[i])
            dp.append(a)
        
        return max(dp)
