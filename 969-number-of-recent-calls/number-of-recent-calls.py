from collections import deque

class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        newerThan = t - 3000
        self.queue.appendleft(t)
        while self.queue[-1] < newerThan:
            self.queue.pop()
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)