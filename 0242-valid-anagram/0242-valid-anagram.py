class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        return sorted(list(s)) == sorted(list(t))