class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0]) - 1
        t, b = 0, len(matrix) - 1
        if matrix[0][0] > target or matrix[-1][-1] < target:
            return False
        while t <= b:
            middle_y = (b - t // 2) + t
            if matrix[middle_y][0] == target:
                return True
            elif matrix[middle_y][0] > target:
                b = middle_y - 1
            else:
                t = middle_y + 1
        if t >= len(matrix) or matrix[t][0] > target:
            t -= 1
        while l <= r:
            middle_x = (r - l // 2) + l
            if matrix[t][middle_x] == target:
                return True
            elif matrix[t][middle_x] > target:
                r = middle_x - 1
            else:
                l = middle_x + 1
        return False