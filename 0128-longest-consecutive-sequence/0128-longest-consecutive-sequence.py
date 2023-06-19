class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unchecked = Counter(nums)
        longest = 0
        for n in nums:
            del unchecked[n]
            x = n + 1
            y = n - 1
            streak = 1
            while x in unchecked:
                del unchecked[x]
                streak += 1
                x += 1
            while y in unchecked:
                del unchecked[y]
                streak += 1
                y -= 1
            longest = max(longest, streak)
        return longest