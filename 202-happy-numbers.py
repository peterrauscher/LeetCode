def isHappyHelper(n, seen):
    if n == 1:
        return True
    digits = [int(i) for i in str(n)]
    if digits in seen:
        return False
    seen.append(digits)
    return isHappyHelper(sum(map(lambda x: x**2, digits)), seen)


class Solution:
    def isHappy(self, n: int) -> bool:
        return isHappyHelper(n, [])
