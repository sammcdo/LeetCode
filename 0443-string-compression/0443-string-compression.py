class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        s = ""
        count = 1
        last = chars[0]
        i = 1
        while True:
            if chars[i] != last:
                if count != 1:
                    s = s + last + str(count)
                else:
                    s = s + last
                last = chars[i]
                count = 0
            if chars[i] == last:
                count += 1
            i += 1
            if i == len(chars):
                if count != 1:
                    s = s + last + str(count)
                else:
                    s = s + last
                break
        
        print(s, last, count)
        print(len(s))
        for i in range(len(s)):
            if len(chars) > i:
                chars[i] = s[i]
            else:
                chars.append(s[i])
        return len(s)
