class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp1 = [nums[0]]
        dp2 = [nums[0]]
        
        hasPositive = False
        for i in range(1, len(nums)):
            a = min(dp1[i-1] + nums[i], nums[i])
            dp1.append(a)
            a = max(dp2[i-1] + nums[i], nums[i])
            dp2.append(a)
            
            if nums[i] > 0:
                hasPositive = True
        
        maximum = max(dp2)
        minimum = min(dp1)

        if hasPositive:
            return max(maximum, sum(nums) - minimum)
        else:
            return min(maximum, sum(nums) - minimum)
