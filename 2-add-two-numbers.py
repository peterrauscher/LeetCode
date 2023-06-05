from typing import Optional, List

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def LinkedList(nums):
    if nums == []:
        return None
    return ListNode(nums[0], LinkedList(nums[1:]))


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        h1 = l1
        prev = ListNode()
        h2 = l2
        carry = 0
        while not (h1 is None or h2 is None):
            sum = h1.val + h2.val + carry
            if sum >= 10:
                carry = 1
            else:
                carry = 0
            h1.val = sum % 10
            prev = h1
            h1 = h1.next
            h2 = h2.next
        finisher = h1 or h2
        prev.next = finisher
        while carry == 1 and not finisher is None:
            sum = finisher.val + carry
            if sum >= 10:
                carry = 1
            else:
                carry = 0
            finisher.val = sum % 10
            prev = finisher
            finisher = finisher.next
        if carry == 1:
            prev.next = ListNode(1, None)
        return l1


s = Solution()
s.addTwoNumbers(LinkedList([2, 4, 9]), LinkedList([5, 6, 4, 9]))
