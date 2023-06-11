class SnapshotArray:
    def __init__(self, length: int):
        self.data = [0 for _ in range(length)]
        self.snapCount = -1
        self.snapshots = []

    def set(self, index: int, val: int) -> None:
        self.data[index] = val

    def snap(self) -> int:
        self.snapshots.append(self.data.copy())
        self.snapCount += 1
        if self.snapCount == 0:
            return 0
        return self.snapCount - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.snapshots[snap_id][index]


snapshotArr = SnapshotArray(3)
snapshotArr.set(0, 5)
snapshotArr.snap()
snapshotArr.set(0, 6)
snapshotArr.get(0, 0)

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
