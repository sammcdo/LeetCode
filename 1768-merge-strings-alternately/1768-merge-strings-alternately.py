class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        dist = max(len(word1), len(word2))

        out = ""
        for i in range(dist):
            if i < len(word1):
                out += word1[i]
            if i < len(word2):
                out += word2[i]
        
        return out