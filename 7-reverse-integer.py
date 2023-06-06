INTMAX = 2147483647
INTMIN = -2147483648


class Solution:
    def reverse(self, x: int) -> int:
        n, neg, result = len(str(x)), 1, 0
        if x < 0:
            x, neg, n = abs(x), -1, n - 1
        for i in range(1, n + 1):
            result += (10 ** (n - i)) * (x % 10)
            x //= 10
        return result * neg


s = Solution()
print(s.reverse(-12345))
