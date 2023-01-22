# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        next_pointer = None
        prev_pointer = None
        curr_pointer = head
        while not curr_pointer == None:
            next_pointer = curr_pointer.next
            curr_pointer.next = prev_pointer
            prev_pointer = curr_pointer
            curr_pointer = next_pointer
        return prev_pointer