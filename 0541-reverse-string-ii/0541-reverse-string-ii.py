class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        k = min(len(s), k)

        i = 0

        final = ""

        while i < len(s):
            tmp = ""
            for j in range(k):
                if i >= len(s):
                    final = final + tmp
                    return final
                tmp = s[i] + tmp
                i += 1
            final = final + tmp
            tmp = ""
            for j in range(k):
                if i >= len(s):
                    final = final + tmp
                    return final
                tmp = tmp + s[i]
                i += 1
            final = final + tmp
        
        return final
            