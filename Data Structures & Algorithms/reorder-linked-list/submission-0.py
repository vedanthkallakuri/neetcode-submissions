# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        head2 = slow.next
        slow.next = None

        prev = None
        while head2:
            nextnode = head2.next
            head2.next = prev
            prev = head2
            head2 = nextnode
        print(2)
        head2 = prev

        while head2:
            next1 = head.next
            next2 = head2.next
            head.next = head2
            head2.next = next1
            head = next1
            head2 = next2
        print(3)
    