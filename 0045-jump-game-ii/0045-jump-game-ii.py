class Solution:
    def jump(self, nums: List[int]) -> bool:
        a = len(nums)
        if a == 1:
            return 0
        if a == 2:
            if nums[0] == 0:
                return 0
            else:
                return 1
        
        if nums[0] == 0:
            return 0
        
        indexes = [a-1]
        for i in range(a-2, -1, -1):
            jumped = i + nums[i]
            if len(indexes) > 1:
                madeJump = False
                for j in range(len(indexes)-1,0,-1):
                    if jumped >= indexes[j-1]:
                        indexes.pop(j)
                        madeJump = True
                if madeJump:
                    indexes.append(i)
            if jumped >= indexes[-1]:
                indexes.append(i)
        
        if 0 in indexes:
            return len(set(indexes)) - 1
        else:
            return 0
            
