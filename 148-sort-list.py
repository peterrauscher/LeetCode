# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        start = head
        while start != None:
            curr = start
            while curr != None:
                if start.val > curr.val:
                    swap = curr.val
                    curr.val = start.val
                    start.val = swap
                curr = curr.next
            start = start.next
        return head
