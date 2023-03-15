def maxSubArray(nums):
    max_sum = nums[0]
    outer_sum = 0
    inner_sum = 0
    for i in range(len(nums)):
        outer_sum = nums[i]
        for j in range(len(nums)):
            if i == j:
                inner_sum = outer_sum
            else:
                inner_sum = inner_sum + nums[j]
            if inner_sum > max_sum:
                max_sum = inner_sum
        inner_sum = outer_sum
    return max_sum

# 6
print(maxSubArray([1,-1,1]))