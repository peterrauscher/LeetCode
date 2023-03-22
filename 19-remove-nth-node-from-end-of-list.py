# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        curr = head
        keep = []
        numToKeep = n + 1
        while curr != None:
            if len(keep) >= numToKeep:
                keep = keep[1:]
            keep.append(curr)
            curr = curr.next
        keep.reverse()
        if n == len(keep):
            return head.next
        elif n == 1:
            keep[n].next = None
        else:
            keep[n].next = keep[n - 2]
        return head
