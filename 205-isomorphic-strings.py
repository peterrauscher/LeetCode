class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapS = list(s)
        mapT = list(t)
        seen_s = []
        seen_t = []
        for i in range(len(s)):
            if s[i] not in seen_s:
                seen_s.append(s[i])
                mapS = [i if x == s[i] else x for x in mapS]
            if t[i] not in seen_t:
                seen_t.append(t[i])
                mapT = [i if x == t[i] else x for x in mapT]
        return mapS == mapT