# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        prev = None
        while head:
            nextnode = head.next
            head.next = prev
            prev = head
            head = nextnode

        head = prev

        if n == 1:
            head = head.next

        else:
            head2 = head
            for i in range(n-2):
                head2 = head2.next

            head2.next = head2.next.next
        
        prev = None
        while head:
            nextnode = head.next
            head.next = prev
            prev = head
            head = nextnode

        return prev