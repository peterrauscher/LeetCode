class Solution:
    def productExceptSelf(self, nums):
        prefix = []
        postfix = [0] * len(nums)
        result = []
        for i in range(len(nums)):
            prod = 1 if i == 0 else prefix[i-1]
            prefix.append(prod * nums[i])
        for i in range(len(nums) - 1, -1, -1):
            prod = 1 if i == (len(nums) - 1) else postfix[i+1]
            postfix[i] = (prod * nums[i])
        for i in range(len(nums)):
            pre = 1 if i == 0 else prefix[i-1]
            post = 1 if i == (len(nums) - 1) else postfix[i+1]
            result.append(pre * post)
        return result