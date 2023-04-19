class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        content = 0

        if len(s) == 0 or len(g) == 0:
            return 0
        
        g = sorted(g)
        s = sorted(s)

        p = len(s)-1
        for i in range(len(g)-1, -1, -1):
            if p >= len(s) or p < 0:
                continue
            
            if s[p] >= g[i]:
                content += 1
                p -= 1

        return content
