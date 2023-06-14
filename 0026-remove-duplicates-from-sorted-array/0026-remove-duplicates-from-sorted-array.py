class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 1:
            return 1
        head = 0
        tail = 0
        unique = 1
        while tail < len(nums):
            if head == tail:
                tail += 1
            else:
                if nums[head] == nums[tail]:
                    tail += 1
                else:
                    if tail - head > 1:
                        nums[head:tail] = [nums[head]]
                        tail = head
                    else:
                        head += 1
                        unique += 1
        return unique