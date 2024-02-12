class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            '(' : ')',
            "{" : "}",
            "[" : "]"
        }
        for c in s:
            if c in brackets:
                stack.append(brackets[c])
            else:
                if not (stack and stack.pop() == c):
                    return False
        return len(stack) == 0