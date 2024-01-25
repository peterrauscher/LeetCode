class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        return [kids_candies + extraCandies >= max_candy for kids_candies in candies]