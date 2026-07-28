# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 0
        def dfs(node, largest):
            nonlocal res
            if not node:
                return

            if node.val >= largest:
                res += 1

            new_largest = max(largest, node.val)
            left = dfs(node.left, new_largest)
            right = dfs(node.right, new_largest)

        dfs(root, root.val)
        return res