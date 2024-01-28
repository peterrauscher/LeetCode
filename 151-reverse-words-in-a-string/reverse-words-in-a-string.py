class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        i = len(s) - 1
        stack = deque()
        while i>=0:
            if s[i] == " ":
                if len(stack) > 0:
                    while len(stack) > 0:
                        res += stack.pop()
                    res += " "
            else:
                stack.append(s[i])
            i -= 1
        while len(stack) > 0:
            res += stack.pop()
        return res.strip()