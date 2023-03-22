# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def getMiddleNode(head):
    tortoise = head
    hare = head
    while hare and hare.next:
        hare = hare.next.next
        if hare:
            tortoise = tortoise.next
    middle = tortoise.next
    tortoise.next = None
    return middle

def mergeInSortedOrder(head1, head2):
    head = None
    curr = None
    if not head1:
        return head2
    if not head2:
        return head1
    while head1 and head2:
        lowest = head1
        if head1.val > head2.val:
            lowest = head2
            head2 = head2.next
        else:
            head1 = head1.next
        if not head:
            head = lowest
        else:
            curr.next = lowest
        curr = lowest
    if head1:
        curr.next = head1
    if head2:
        curr.next = head2
    return head

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        mid = getMiddleNode(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return mergeInSortedOrder(left, right)