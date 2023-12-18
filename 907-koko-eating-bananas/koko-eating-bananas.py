from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minK = max(piles)
        lowK, highK = 1, minK
        while lowK <= highK:
            k = ((highK - lowK) // 2) + lowK
            remaining = h
            i = 0
            while i  < len(piles) and remaining > 0:
                remaining -= ceil(piles[i] / k)
                i += 1
            if i == len(piles) and remaining >= 0:
                highK = k - 1
                minK = min(minK, k)
            else:
                lowK = k + 1
        return minK