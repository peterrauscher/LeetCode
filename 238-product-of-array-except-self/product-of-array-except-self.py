class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r = []
        runningProduct = 1
        for num in nums[::-1]:
            r.append(runningProduct)
            runningProduct *= num
        runningProduct = 1
        for i in range(len(nums)):
            tmp = nums[i]
            nums[i] = r[-(i + 1)] * runningProduct
            runningProduct *= tmp
        return nums
            
