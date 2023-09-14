class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        
        maxVol = 0
        while start < end:
            vol = min(height[start], height[end]) * (end - start)
            
            if vol > maxVol:
                maxVol = vol
            
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        
        return maxVol
