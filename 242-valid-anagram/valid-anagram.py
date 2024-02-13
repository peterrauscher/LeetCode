class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count, t_count = {}, {}
        for c in s:
            s_count[c] = s_count.get(c, 0) + 1
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1
        if not len(t_count) == len(s_count):
            return False
        for k in t_count.keys():
            if not t_count.get(k, 0) == s_count.get(k, 0):
                return False
        return True