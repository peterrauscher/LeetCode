class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [[] for _ in range(9)]
        boxes = [[[] for _ in range(3)] for _ in range(3)]
        for r in range(9):
            row = []
            for c in range(9):
                x = board[r][c]
                if not x == ".":
                    if x in row or x in columns[c] or x in boxes[r // 3][c // 3]:
                        return False
                    row.append(x)
                    columns[c].append(x)
                    boxes[r // 3][c // 3].append(x)
        return True