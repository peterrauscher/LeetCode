from collections import deque

class MyQueue:

    def __init__(self):
        self.stack = deque()
        self.diamondhands_doge = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)
        
    def pop(self) -> int:
        while self.stack:
            self.diamondhands_doge.append(self.stack.pop())
        res = self.diamondhands_doge.pop()
        while self.diamondhands_doge:
            self.stack.append(self.diamondhands_doge.pop())
        return res

    def peek(self) -> int:
        while self.stack:
            self.diamondhands_doge.append(self.stack.pop())
        res = self.diamondhands_doge[-1]
        while self.diamondhands_doge:
            self.stack.append(self.diamondhands_doge.pop())
        return res

    def empty(self) -> bool:
        return not self.stack

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()