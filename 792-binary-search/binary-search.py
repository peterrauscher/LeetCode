class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            middle = ((r - l) // 2) + l
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                r = middle
            else:
                l = middle + 1
        return -1