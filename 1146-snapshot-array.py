class SnapshotArray:
    def __init__(self, length: int):
        # A 2D list of "tuples" lists of type (value, number of snapshots)
        self.history = []
        self.data = [0 for _ in range(length)]
        self.snapCount = -1

    def set(self, index: int, val: int) -> None:
        self.data[index] = val

    def snap(self) -> int:
        if not self.history:
            self.history = [[[n, 1]] for n in self.data]
        for i, l in enumerate(self.history):
            if l[-1][0] == self.data[i]:
                l[-1][1] += 1
            else:
                l.append([self.data[i], 1])
        self.snapCount += 1
        return self.snapCount

    def get(self, index: int, snap_id: int) -> int:
        snap_id += 2
        for item in self.history[index]:
            snap_id = snap_id - item[1]
            if snap_id <= 0:
                return item[0]
