class Solution:
    def partitionString(self, s: str) -> int:
        sub = ""
        count = 1

        for i in range(len(s)):
            if s[i] in sub:
                sub = s[i]
                count += 1
            else:
                sub += s[i]
        
        return count