class Solution:
    def addBinary(self, a: str, b: str) -> str:
        for i in range(max(0, len(b) - len(a))):
            a = "0" + a
        
        for i in range(max(0, len(a) - len(b))):
            b = "0" + b
        
        carry = 0
        final = ""
        for i in range(len(a)-1, -1, -1):
            x = int(a[i])
            y = int(b[i])
            f = (x + y + carry) % 2
            carry = (x + y + carry) // 2
            final = str(f) + final
        
        if carry:
            final = "1"+final
        return final