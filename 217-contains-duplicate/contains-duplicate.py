class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        for i in range(1, len(nums)):
            if sorted_nums[i-1] ==sorted_nums[i]:
                return True
        return False