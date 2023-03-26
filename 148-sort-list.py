# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def getMiddleNode(self, head):
        if not head or not head.next:
            return head
        tortoise = head
        prev = head
        hare = head
        while hare.next != None and hare.next.next != None:
            tortoise = tortoise.next
            hare = hare.next.next
        return tortoise

    def mergeInSortedOrder(self, head1, head2):
        if head1 == None:
            return head2
        if head2 == None:
            return head1
        if head2.val > head1.val:
            temp = head1

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        mid = getMiddleNode(head)
