class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        remaining = list(s)
        for c in t:
            if remaining == []:
                return True
            if c == remaining[0]:
                remaining = remaining[1:]
        return remaining == []