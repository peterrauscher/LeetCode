class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies) - extraCandies
        return [kids_candies >= max_candy for kids_candies in candies]