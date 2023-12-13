from collections import deque

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(s, numOpen, numClosed):
            if 2 * n == (numOpen + numClosed):
                res.append(s)
            elif numOpen == numClosed:
                backtrack(s + "(", numOpen + 1, numClosed)
            elif numOpen > numClosed:
                backtrack(s + ")", numOpen, numClosed + 1)
                if not numOpen == n:
                    backtrack(s + "(", numOpen + 1, numClosed)
        
        backtrack("(", 1, 0)
        return res