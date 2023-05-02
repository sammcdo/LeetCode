class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negCount = 0
        for i in nums:
            if i == 0:
                return 0
            if i < 0:
                negCount += 1
        
        return -1 if negCount % 2 == 1 else 1