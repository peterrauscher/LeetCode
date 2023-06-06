class Solution:
    def isArithmeticProgression(self, arr: List[int]) -> bool:
        # Base case, only one difference so always true
        if len(arr) == 2:
            return True
        # Define the difference between the first and second element
        diff = arr[0] - arr[1]
        for i in range(len(arr) - 1):
            # If at any point the difference is not the same, return False
            if not diff == arr[i] - arr[i + 1]:
                return False
        return True

    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        # If the difference between each consecutive element is the same, then it must be in ascending or descending order
        return self.isArithmeticProgression(
            sorted(arr)
        ) or self.isArithmeticProgression(sorted(arr)[::-1])
