class Solution:
    def isPalindrome(self, x: int) -> bool:
        def isPalindromeTailRec(x, magnitude, soFar=True):
            if x == 0 or not soFar or magnitude == 1:
                return soFar
            return isPalindromeTailRec(
                (x % (10 ** (magnitude - 1))) // 10,
                magnitude - 2,
                soFar and ((x % 10) == x // (10 ** (magnitude - 1))),
            )

        if x < 0:
            return False
        magnitude = 0
        while x >= 10**magnitude:
            magnitude += 1
        return isPalindromeTailRec(x, magnitude)


s = Solution()
print(s.isPalindrome(12321))
