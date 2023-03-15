class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        prefix = ""
        for i in range(min(map(lambda s: len(s), strs))):
            if all(map(lambda s: s[i] == strs[0][i], strs)):
                prefix += strs[0][i]
            else:
                return prefix
        return prefix
