class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = Counter(s)
        length = 0
        if len(letters) == 1: return letters[next(iter(letters))]
        for letter, count in letters.items():
            if length % 2 == 0 and count % 2 == 1:
                length += count
            else:
                length += (count // 2) * 2
        return length