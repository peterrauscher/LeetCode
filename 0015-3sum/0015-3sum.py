class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = list(sorted(nums))
        addsToZero = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]: continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                thisSum = nums[i] + nums[l] + nums[r]
                if thisSum < 0:
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif thisSum > 0:
                    r -= 1
                    while nums[r] == nums[r+1] and r > l:
                        r -= 1
                else:
                    addsToZero.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                    r -= 1
                    while nums[r] == nums[r+1] and r > l:
                        r -= 1

        return addsToZero