class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True
        if len(nums) == 2:
            if nums[0] == 0:
                return False
            else:
                return True
        
        if nums[0] == 0:
            return False
        
        indexes = [len(nums)-1]
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= indexes[-1]:
                indexes.append(i)
        
        if 0 in indexes:
            return True
        else:
            return False
            
