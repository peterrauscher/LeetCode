class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        for i in range(len(s)):
            length = 0
            seen = []
            for comp in s[i:]:
                if comp in seen:
                    break
                else:
                    length += 1
                    seen.append(comp)
            max_length = max(length, max_length)
            length = 0
            seen = []
        return max_length


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
