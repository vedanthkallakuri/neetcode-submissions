# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = collections.deque()
        queue.append(root)
        res = []

        while queue:
            sublist = []
            level = len(queue)
            for i in range(level):
                node = queue.popleft()
                if node:
                    sublist.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if sublist:
                res.append(sublist)

        return res