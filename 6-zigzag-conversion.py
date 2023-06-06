class Solution:
    def convert_old(self, s: str, numRows: int) -> str:
        print(s)
        print("".join([str(i % numRows) for i in range(len(s))]))
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

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        output = s[::1]
        for i, c in enumerate(s):
            if i % numRows == 0:
                output[i] = i / numRows
            else:
        return "".join(output)


s = Solution()
print(s.convert_old(s="0123456789", numRows=3))
#                      159246837
#                      012012012
