# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def helper(root):
            if not root: return [0, None]
            leftH, leftLCA = helper(root.left)
            rightH, rightLCA = helper(root.right)
            if leftH > rightH: return [leftH+1, leftLCA]
            if rightH > leftH: return [rightH+1, rightLCA]
            return [leftH+1, root]
        
        return helper(root)[1]