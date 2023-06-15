class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s, t = list(s), list(t)
        s.sort()
        t.sort()
        if not len(s) == len(t):
            return False
        for i in range(len(s)):
            if not s[i] == t[i]:
                return False
        return True