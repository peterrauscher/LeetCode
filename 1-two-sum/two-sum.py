class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in targets:
                return [i, targets[need]]
            else:
                targets[num] = i
