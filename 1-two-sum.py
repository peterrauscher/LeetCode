# Brute force solution, there's a better way to do this

def twoSum(nums, target):
    for i in range(len(nums)):
        x = nums[i]
        for j in range(i+1, len(nums)):
            y = nums[j]
            if x + y == target:
                return [i, j]

print (twoSum([3,2,4], 6))