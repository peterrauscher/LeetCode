# Brute force solution, there's a better way to do this
class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        for i in range(len(nums)):
            x = nums[i]
            for j in range(i+1, len(nums)):
                y = nums[j]
                if x + y == target:
                    return [i, j]