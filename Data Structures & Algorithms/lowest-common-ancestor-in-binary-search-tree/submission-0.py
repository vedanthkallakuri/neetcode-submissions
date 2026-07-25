# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        p1 = self.returnParents(root, p)
        p2 = self.returnParents(root, q)

        p1_set = set(p1)
        return next((item for item in p2 if item in p1_set), None)
        
    
    def returnParents(self, root, target):
        if not root:
            return []
        
        if root.val == target.val:
            return [root]

        left = self.returnParents(root.left, target)
        right = self.returnParents(root.right, target)
        if len(left) > 0:
            left.append(root)
            return left
        if len(right) > 0:
            right.append(root)
            return right
        else:
            return []

            
        