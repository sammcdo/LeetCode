import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums = [-i for i in nums]
        heapq.heapify(nums)
        
        while len(nums) > k:
            heapq.heappop(nums)
        
        return nums[0]
            