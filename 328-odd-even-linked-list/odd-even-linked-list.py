# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head
        oddCurr = head
        evenHead = head.next
        evenCurr = evenHead
        while oddCurr and oddCurr.next:
            oddCurr.next = oddCurr.next.next
            if oddCurr.next: oddCurr = oddCurr.next
            if evenCurr and evenCurr.next:
                evenCurr.next = evenCurr.next.next
                evenCurr = evenCurr.next
        oddCurr.next = evenHead
        return head