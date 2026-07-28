# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, left, right):
            if not node:
                return True
            
            if not left < node.val < right:
                return False

            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
            # if node.left: 
            #     left_sat = node.left.val < node.val and node.left.val > interval[0]
            # if node.right: 
            #     right_sat = node.right.val > node.val and node.right.val < interval[1]
    

            # sat = left_sat and right_sat
            # return sat and dfs(node.left, [interval[0], node.val]) and dfs(node.right, [node.val, interval[1]])

        return dfs(root, float('-inf'), float('inf'))