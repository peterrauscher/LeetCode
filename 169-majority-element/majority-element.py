class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorityCount = (len(nums) // 2) + 1
        seen = {}
        for n in nums:
            seen[n] = seen.get(n, 0) + 1
            if seen[n] == majorityCount:
                return n