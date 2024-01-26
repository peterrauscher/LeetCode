class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1:
            return n == 1 and flowerbed[0] == 0
        i = 0
        while i < len(flowerbed):
            if flowerbed[i]:
                i += 2
            else:
                if (i == 0 and not flowerbed[i+1]) or (i == len(flowerbed) - 1 and not flowerbed[i-1]) or not (flowerbed[i - 1] or flowerbed[i+1]):
                    n -= 1
                    i += 2
                else:
                    i += 1
        return n <= 0