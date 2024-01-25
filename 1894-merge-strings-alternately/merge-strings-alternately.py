class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word_result = []
        difference = len(word1) - len(word2)
        go_to = len(word1) if difference < 0 else len(word2)
        for i in range(go_to):
            word_result.append(word1[i])
            word_result.append(word2[i])

        if difference > 0:
            word_result += word1[-difference:]
        elif difference < 0:
            word_result += word2[difference:]
        
        return ''.join(word_result)