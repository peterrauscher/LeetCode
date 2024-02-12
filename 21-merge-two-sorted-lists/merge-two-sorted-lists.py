# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
        newHead = ListNode()
        curr = newHead
        curr1 = list1
        curr2 = list2
        while True:
            if not curr1:
                curr.next = curr2
                return newHead.next
            if not curr2:
                curr.next = curr1
                return newHead.next
            if curr1.val <= curr2.val:
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next
        return newHead.next