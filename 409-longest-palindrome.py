class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        length = 0
        for n in freq.values():
            length += (n // 2) * 2
        if length < len(s):
            length += 1
        return length

## It works, but there's definitely a better way to do this.