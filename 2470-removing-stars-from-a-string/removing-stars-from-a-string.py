class Solution:
    def removeStars(self, s: str) -> str:
        length = len(s)
        i = 0
        while i < length:
            if s[i] == "*":
                s = s[0:i-1] + s[i+1:]
                length -= 2
                i -= 1
            else:
                i += 1
        return s