class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}

        m = nums[0]
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
            if d[n] > d[m]:
                    m = n
        
        return m
