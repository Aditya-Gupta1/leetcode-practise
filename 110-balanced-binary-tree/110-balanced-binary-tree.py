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
        rightH = self.helper(root.right)
        if abs(leftH - rightH) > 1:
            self.ans = False
        return max(leftH, rightH) + 1
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        self.helper(root)
        return self.ans