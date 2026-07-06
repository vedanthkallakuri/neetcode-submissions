# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head is None or head.next is None:
            return False
        ptr1 = head
        ptr2 = head.next

        while ptr1 != ptr2:
            if ptr2 is None:
                return False
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            if ptr2:
                ptr2 = ptr2.next
        return True