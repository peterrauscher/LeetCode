class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        table = [[] for _ in range(numRows)]
        y = 0
        direction = 1
        for c in s:
            table[y].append(c)
            if y == numRows - 1 and y != 0:
                direction = -1
            else:
                if y == 0:
                    direction = 1
            y += direction
        return "".join(["".join(row) for row in table])
