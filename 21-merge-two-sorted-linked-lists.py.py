# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()
        curr = new_head
        pointer1 = list1
        pointer2 = list2
        while True:
            if pointer1 == None:
                curr.next = pointer2
                break
            if pointer2 == None:
                curr.next = pointer1
                break
            if pointer1.val <= pointer2.val:
                curr.next = pointer1
                pointer1 = pointer1.next
            else:
                curr.next = pointer2
                pointer2 = pointer2.next
            curr = curr.next
        return new_head.next
