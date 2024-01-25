class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowel_at = []
        vowel_seq = []
        l = list(s)
        for i in range(len(s)):
            if s[i] in vowels:
                vowel_at.append(i)
                vowel_seq.append(s[i])
        vowel_seq.reverse()
        for i in range(len(vowel_at)):
            l[vowel_at[i]] = vowel_seq[i]
        return ''.join(l)