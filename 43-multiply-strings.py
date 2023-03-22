# I personally HATE this problem. Why would we not leverage basic language features like type
# conversions? This is a really complex solution to an extremely easy problem.


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        yellowPages = {
            str(i): i for i in range(10)
        }  # Get it? Cause its a number lookup. Hehe.
        num1_int = 0
        i = 0
        for c in num1[::-1]:
            num1_int += yellowPages[c] * 10**i
            i += 1
        num2_int = 0
        i = 0
        for c in num2[::-1]:
            num2_int += yellowPages[c] * 10**i
            i += 1
        return str(num1_int * num2_int)


s = Solution()
print(s.multiply("2", "3"))
