class Solution:
    def divides(self, divisor: str, dividend: str):
        if not len(dividend) % len(divisor) == 0:
            return False
        return dividend.replace(divisor, "") == ""

    def gcdHelper(self, str1: str, str2: str, l: int, tried):
        if l == len(str2):
            return ""
        gcd = str2[l:]
        if gcd not in tried:
            if self.divides(gcd, str1) and self.divides(gcd, str2):
                return gcd
            tried.add(gcd)
        return self.gcdHelper(str1, str2, l + 1, tried)

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            return self.gcdHelper(str2, str1, 0, set())
        else:
            return self.gcdHelper(str1, str2, 0, set())