class Solution:
    def longestPalindrome(self, words):
        longest = 0
        seen = {}
        for word in words:
            count = seen.get(word)
            if count == None:
                seen[word] = 1
            else:
                seen[word] = count + 1
        reversedSeen = []
        existsMiddle = False
        for word, count in seen.items():
            # Skip if we've already seen this word's reverse before, we handled its count already.
            if not word in reversedSeen:
                rev = word[::-1]
                # If the word is a double (e.g. "xx" or "yy") then
                if word == rev:
                    # Check if it's an even or odd count,
                    if count % 2 == 1:
                        if not existsMiddle:
                            # If we haven't, add this word to the middle
                            longest += count
                            existsMiddle = True
                        else:
                            # If we have, only add the next lowest even amount
                            longest += (count // 2) * 2
                    # If it's even, we can add all of them
                    else:
                        longest += count
                # If it's not a double, but its reverse is also in the list (e.g. "cl" and "lc")
                elif rev in seen:
                    # Then add the amount they both share
                    longest += min(count, seen[rev]) * 2
                reversedSeen.append(rev)
        return (longest) * 2


tests = [
    ["dd", "aa", "bb", "dd", "aa", "dd", "bb", "dd", "aa", "cc", "bb", "cc", "dd", "cc"]
]
for test in tests:
    s = Solution()
    print("Testing with words = [" + ", ".join(test) + "]")
    print("Longest palindrome: " + str(s.longestPalindrome(test)))
    print("================================================================")
