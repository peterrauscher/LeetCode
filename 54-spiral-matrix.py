def spiralHelper(matrix, n, m, x, y, xdir, ydir, reslength):
    if reslength == len(matrix) * len(matrix[0]):
        return []
    if x == (n - 1) and y == (len(matrix) - m):
        xdir = 0
        ydir = 1
    elif x == (len(matrix[0]) - n) and y == (len(matrix) - m):
        if not xdir == 1:
            n -= 1
        xdir = 1
        ydir = 0
    elif x == (n - 1) and y == (m - 1):
        xdir = -1
        ydir = 0
    elif x == (len(matrix[0]) - n) and y == (m - 1):
        if not ydir == -1:
            m -= 1
        xdir = 0
        ydir = -1
    reslength += 1
    return [matrix[y][x]] + spiralHelper(
        matrix, n, m, x + xdir, y + ydir, xdir, ydir, reslength
    )


class Solution:
    def spiralOrder(self, matrix):
        return spiralHelper(matrix, len(matrix[0]), len(matrix), 0, 0, 1, 0, 0)


sMatrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

s = Solution()
print(s.spiralOrder(sMatrix))
