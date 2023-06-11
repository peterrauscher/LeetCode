class Node:
    def __init__(self, n: int, next=None, snaps=1):
        self.n = n
        self.next = next
        self.snaps = snaps


class LinkedList:
    def __init__(self, head):
        self.head = head
        self.tail = None

    def get(self, i: int) -> int:
        at = 0
        curr = self.head
        while at <= i and curr.next is not None:
            if (at + curr.snaps) > i:
                return curr.n
            at = at + curr.snaps
            curr = curr.next
        return curr.n

    def insertIfDifferent(self, n: int) -> None:
        curr = self.tail
        if curr is None:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
        if curr.n == n:
            curr.snaps += 1
        else:
            curr.next = Node(n)
            self.tail = curr.next


class SnapshotArray:
    def __init__(self, length: int):
        self.heads = None
        self.data = [0 for _ in range(length)]
        self.snapCount = -1

    def set(self, index: int, val: int) -> None:
        self.data[index] = val

    def snap(self) -> int:
        if self.heads == None:
            self.heads = [LinkedList(Node(n)) for n in self.data]
        else:
            for i, ll in enumerate(self.heads):
                ll.insertIfDifferent(self.data[i])
        self.snapCount += 1
        return self.snapCount

    def get(self, index: int, snap_id: int) -> int:
        return self.heads[index].get(snap_id)


# ["SnapshotArray","snap","snap","set","snap","get","set","get","snap","get"]
# [[1],[],[],[0,4],[],[0,1],[0,12],[0,1],[],[0,3]]
# Expected: [null,0,1,null,2,0,null,0,3,12]
events = [
    "SnapshotArray",
    "snap",
    "snap",
    "set",
    "snap",
    "get",
    "set",
    "get",
    "snap",
    "get",
]
datas = [[1], [], [], [0, 4], [], [0, 1], [0, 12], [0, 1], [], [0, 3]]

sa = SnapshotArray(datas[0][0])
for i in range(1, len(events)):
    if events[i] == "snap":
        print(sa.snap())
    elif events[i] == "set":
        sa.set(datas[i][0], datas[i][1])
    elif events[i] == "get":
        print(sa.get(datas[i][0], datas[i][1]))
print("Done!")
