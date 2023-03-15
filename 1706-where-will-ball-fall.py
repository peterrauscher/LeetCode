from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        destination_array = []
        for col in range(len(grid[0])):
            ball_pos = col
            for i in range(len(grid)):
                # 1 = slopes down (to right)
                # -1 = slopes up (to left)
                slope = grid[i][ball_pos]
                if slope == 1:
                    if ball_pos == len(grid[i]) - 1 or grid[i][ball_pos + 1] == -1:
                        ball_pos = -1
                        break
                elif slope == -1:
                    if ball_pos == 0 or grid[i][ball_pos - 1] == 1:
                        ball_pos = -1
                        break
                ball_pos += slope
            destination_array.append(ball_pos)
        return destination_array


s = Solution()
print(s.findBall([[-1]]))
