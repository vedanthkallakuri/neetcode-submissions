"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        pairings = {}
        pairings[None] = None

        ptr = head
        while ptr:
            pairings[ptr] = Node(ptr.val)
            ptr = ptr.next
        
        ptr = head
        while ptr:
            newNode = pairings[ptr]
            newNextNode = pairings[ptr.next]
            newRandNode = pairings[ptr.random]

            newNode.next = newNextNode
            newNode.random = newRandNode

            ptr = ptr.next

        return pairings[head]
        

