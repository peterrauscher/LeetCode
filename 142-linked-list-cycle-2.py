# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cops = head
        robbers = head
        while True:
            if cops == None or robbers == None or robbers.next == None:
                return None
            cops = cops.next
            robbers = robbers.next.next
            if cops == robbers:
                break
        cops = head
        while not (cops == robbers):
            cops = cops.next
            robbers = robbers.next
        return cops