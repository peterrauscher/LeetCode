cache = {}
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        for i in [1, 2]:
            m = n - i
            if not m in cache:
                cache[m] = self.climbStairs(m)
        return cache[n - 1] + cache[n - 2]