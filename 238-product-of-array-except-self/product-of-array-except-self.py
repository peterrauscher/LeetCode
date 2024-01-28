class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        running = 1
        for i in range(len(nums)):
            running *= nums[i]
            prefix.append(running)
        running = 1
        for i in range(len(nums) - 1, -1, -1):
            running *= nums[i]
            suffix.append(running)
        suffix.reverse()
        answer = [suffix[1]]
        for i in range(1, len(nums) - 1):
            answer.append(prefix[i - 1] * suffix[i + 1])
        answer.append(prefix[len(nums) - 2])
        return answer