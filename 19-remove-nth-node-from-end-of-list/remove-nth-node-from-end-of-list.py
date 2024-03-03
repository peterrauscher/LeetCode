# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        end = deque()
        while curr:
            end.append(curr)
            if len(end) > n + 1:
                end.popleft()
            curr = curr.next
        if len(end) == n: head = head.next
        else:
            prev = end.popleft()
            curr = prev.next.next if prev.next else None
            prev.next = curr
        return head