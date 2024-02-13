class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
            letters = Counter(magazine)
            for c in ransomNote:
                if (c not in letters) or (letters[c] == 0):
                    return False
                letters[c] -= 1
            return True
