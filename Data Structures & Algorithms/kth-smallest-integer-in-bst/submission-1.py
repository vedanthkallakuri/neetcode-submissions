# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        def dfs(node):
            nonlocal count
            if not node:
                return [False, None]
            
            left = dfs(node.left)
            if left[0]:
                return [True, left[1]]
            count += 1
            if count == k:
                return [True, node.val]
            right = dfs(node.right)
            if right[0]:
                return [True, right[1]]
            
            else:
                return [False, None]

        [b, res] = dfs(root)
        return res