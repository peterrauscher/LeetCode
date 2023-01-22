# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# First solution, beats 75% of runtimes and 50% of memory usage. However, a better solution could likely
# run in just one traversal, rather than this one which runs in one and a half.
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        curr = head
        while not curr == None:
            curr = curr.next
            length = length + 1
        curr = head
        for i in range(length // 2):
            curr = curr.next
        return curr

# This solution, the pseudocode for which I found online, beats the above solution. It runs in just one traversal.
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while True:
            if slow == None:
                break
            if fast == None:
                break
            if fast.next == None:
                break
            slow = slow.next
            fast = fast.next.next
        return slow