# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        if not root: return 0
        if not root.left and not root.right: return 1
        
        leftH = self.helper(root.left)
        if leftH == -1: return -1
        
        rightH = self.helper(root.right)
        if rightH == -1: return -1
        
        if abs(leftH - rightH) > 1: return -1
        
        return max(leftH, rightH) + 1
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root) != -1