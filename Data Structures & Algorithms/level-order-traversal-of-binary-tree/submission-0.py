# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        res = []

        while queue:
            sublist = []
            sublistNodes = []
            while queue:
                node = queue.popleft()
                sublistNodes.append(node)
                sublist.append(node.val)
            res.append(sublist)

            for node in sublistNodes:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res