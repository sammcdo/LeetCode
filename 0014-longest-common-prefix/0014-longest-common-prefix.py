class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min([len(w) for w in strs])

        if len(strs) == 1: return strs[0]

        count = 0
        failed = False
        for i in range(shortest):
            a = strs[0][i]
            for w in range(1,len(strs)):
                if strs[w][i] == a:
                    continue
                else:
                    failed = True
            if failed:
                break
            count += 1
        return strs[0][0:count]