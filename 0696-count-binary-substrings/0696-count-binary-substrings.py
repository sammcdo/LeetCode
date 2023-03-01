class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 0

        found = 0

        char = s[0]
        count = 1
        newCount = 0
        for i in range(1, len(s)):
            if s[i] != char and newCount == 0:
                found += 1
                newCount += 1
            
            elif s[i] != char and count > newCount:
                found += 1
                newCount += 1
            
            elif s[i] != char and count <= newCount:
                newCount += 1
            
            elif s[i] == char and newCount > 0:
                count = newCount
                char = s[i-1]
                newCount = 1
                found += 1
            
            elif s[i] == char and newCount == 0:
                count += 1
        
        return found