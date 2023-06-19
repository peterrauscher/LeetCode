class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            jtarget = target - numbers[i]
            upper, lower = len(numbers) - 1, i + 1
            while lower <= upper:
                middle = (upper + lower) // 2
                if numbers[middle] == jtarget:
                    return [i + 1, middle + 1]
                elif numbers[middle] > jtarget:
                    upper = middle - 1
                else:
                    lower = middle + 1