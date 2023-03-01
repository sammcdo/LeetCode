class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        open = ["(", "[", "{"]
        close = [")", "]", "}"]

        areOpen = []
        for i in range(0, len(s)):
            if s[i] in open:
                areOpen.append(s[i])
            if s[i] in close:
                o = open[close.index(s[i])]
                
                if o in areOpen:
                    if o == areOpen[-1]:
                        areOpen.pop()
                    else:
                        return False
                else:
                    return False
        
        if len(areOpen) == 0:
            return True
