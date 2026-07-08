# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        currNode = ListNode()
        head = currNode
        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next

            if (val % 10) - val != 0:
                carry = 1
                val = val - 10
            else:
                carry = 0

            currNode.val = val
            if l1 or l2:
                nextNode = ListNode()
                currNode.next = nextNode
                currNode = nextNode
            elif carry:
                nextNode = ListNode()
                currNode.next = nextNode
                nextNode.val = carry
                nextNode.next = None

        return head
