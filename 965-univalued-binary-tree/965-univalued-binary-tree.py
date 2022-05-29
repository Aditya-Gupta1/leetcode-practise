# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        if not root.right and not root.left: return True
        left, right = True, True
        if root.left:
            if  root.left.val == root.val:
                left = self.isUnivalTree(root.left)
            else:
                return False
        if root.right:
            if root.right.val == root.val:
                right = self.isUnivalTree(root.right)
            else:
                return False
        return left and right