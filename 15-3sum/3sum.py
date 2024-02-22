class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        trips = []
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]: continue
            seen = {}
            target = -sorted_nums[i]
            for j in range(i+1, len(sorted_nums)):
                x = sorted_nums[j]
                y = target - x
                if y in seen:
                    if j > i+1 and j < len(sorted_nums) - 1 and sorted_nums[j] == sorted_nums[j+1]: continue
                    trips.append([sorted_nums[i], sorted_nums[j], y])
                seen[x] = j
        return trips