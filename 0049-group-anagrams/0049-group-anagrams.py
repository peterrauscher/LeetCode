class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in range(len(strs)):
            s = str(sorted(strs[i]))
            if s in seen:
                seen[s].append(i)
            else:
                seen[s] = [i]
        return [[strs[n] for n in v] for k, v in seen.items()]