# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        maximum = 0
        length = 0
        while curr:
            length += 1
            curr = curr.next
        index = 0
        curr = head
        stack = []
        while index < length // 2:
            stack.append(curr.val)
            index += 1
            curr = curr.next
        while curr:
            maximum = max(maximum, curr.val + stack.pop())
            curr = curr.next
        return maximum